# Sistem Deteksi Kebakaran Berbasis IoT
Proyek ini merupakan pengembangan sistem deteksi kebakaran dini yang memanfaatkan teknologi Internet of Things (IoT). Sistem ini dirancang untuk memantau suhu, kelembaban, dan konsentrasi gas berbahaya secara real-time.

## Komponen Utama:

### Hardware:
ESP8266: Berfungsi sebagai mikrokontroler yang mengolah data dari sensor dan mengirimkannya ke Firebase melalui Wi-Fi.
Sensor DHT11: Mengukur suhu dan kelembaban udara.

Sensor MQ-135: Mendeteksi gas berbahaya dan asap.
LED Indikator: Menyala secara otomatis sebagai peringatan fisik ketika terdeteksi kondisi berbahaya.

### Software:
Firebase: Digunakan sebagai basis data real-time untuk menyimpan data sensor yang dikirim oleh ESP8266.
HTML dan JavaScript: Digunakan untuk membangun antarmuka web yang menampilkan data sensor dalam bentuk teks dan grafik.

## Cara Kerja Sistem:
Sensor DHT11 dan MQ-135 membaca kondisi lingkungan.
Data sensor diolah oleh mikrokontroler ESP8266 dan dikirim ke Firebase melalui koneksi Wi-Fi.
Pengguna dapat memantau data tersebut secara 
real-time melalui antarmuka web.
Sistem akan memberikan respons otomatis jika suhu melebihi 50∘ C atau kadar gas melebihi 1000 ppm. Respons ini berupa indikator LED yang menyala pada perangkat keras dan perubahan status "Aman" menjadi "Bahaya" pada antarmuka web.

## Manfaat Proyek:
Proyek ini membuktikan bahwa sistem deteksi kebakaran dini yang terjangkau dan efektif dapat dibangun menggunakan kombinasi perangkat keras yang efisien dan platform cloud. Sistem ini memberikan solusi pemantauan jarak jauh yang dapat meningkatkan keselamatan di lingkungan rumah tangga atau bangunan kecil menengah.
