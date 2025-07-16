import machine
import dht
import time
import math
import network
import urequests  # Modul HTTP di MicroPython

# --- Konfigurasi Wi-Fi ---
SSID = 'RT03RW04'
PASSWORD = 'TUTIK058'

# --- Firebase URL ---
FIREBASE_URL = 'https://uas-io-default-rtdb.firebaseio.com/.json'

# --- Konstanta MQ135 ---
RLOAD = 10.0
RZERO = 76.63
PARA = 116.6020682
PARB = 2.769034857

# --- Fungsi koneksi Wi-Fi ---
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Menghubungkan ke Wi-Fi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Tersambung ke Wi-Fi:", wlan.ifconfig())

# --- Fungsi MQ135 ---
def read_adc(pin):
    adc = machine.ADC(pin)
    return adc.read()

def calculate_resistance(adc_value):
    if adc_value == 0:
        return -1
    return (1023. / adc_value - 1.) * RLOAD

def get_ppm(rs):
    return PARA * math.pow(rs / RZERO, -PARB)

# --- Inisialisasi perangkat ---
dht_sensor = dht.DHT11(machine.Pin(2))     # GPIO2 (D4)
mq135_pin = 0                               # ADC0 (A0)
led = machine.Pin(14, machine.Pin.OUT)      # GPIO14 (D5)

# --- Ambang batas ---
PPM_THRESHOLD = 1000
TEMP_THRESHOLD = 50

# --- Hubungkan ke Wi-Fi ---
connect_wifi(SSID, PASSWORD)

# --- Loop utama ---
while True:
    try:
        # Baca suhu & kelembapan
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        # Baca dan hitung ppm dari MQ135
        adc_value = read_adc(mq135_pin)
        rs = calculate_resistance(adc_value)
        ppm = get_ppm(rs)

        # Tampilkan ke serial
        print("Suhu: {}°C, Kelembapan: {}%, PPM: {:.2f}".format(temperature, humidity, ppm))

        # Kontrol LED
        if temperature > TEMP_THRESHOLD and ppm > PPM_THRESHOLD:
            led.on()
        else:
            led.off()

        # Kirim data ke Firebase
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "ppm": round(ppm, 2)
        }

        response = urequests.put(FIREBASE_URL, json=data)
        print("Data terkirim:", response.text)
        response.close()

    except Exception as e:
        print("Terjadi kesalahan:", e)

    time.sleep(1)  # jeda pengiriman 1 detik