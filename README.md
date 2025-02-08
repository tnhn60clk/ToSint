🛠 Sistem Bilgi Toplayıcı (System Info Collector)
📌 Açıklama
Bu Python tabanlı araç, sistemin donanım ve yazılım bilgilerini toplar ve JSON formatında kaydeder.

CPU, RAM, disk ve ağ bilgilerini toplar.
Antivirüs, güvenlik duvarı ve güncellemeleri kontrol eder.
Yüklü yazılımları ve çalışan süreçleri listeler.
Eksik kütüphaneleri otomatik yükler, böylece her ortamda sorunsuz çalışır.
📦 Kullanılan Kütüphaneler
Bu araç, aşağıdaki Python kütüphanelerini kullanır:

bash
Kopyala
Düzenle
psutil, wmi, socket, json, os, platform, time, getpass, subprocess, win32com.client, datetime
Not: Eğer bir kütüphane eksikse, program başlatıldığında otomatik olarak yükleyecektir.

💻 Kullanım
Python ortamında çalıştırmak için:

bash
Kopyala
Düzenle
python system_info.py
Ya da .exe haline çevrilmiş versiyonunu doğrudan çalıştırabilirsin.

📂 Çıktı Dosyası
Toplanan veriler system_info.json dosyasına kaydedilir.

🚀 .EXE Olarak Kullanım
Eğer Python yüklü değilse ve doğrudan çalıştırmak istiyorsan .exe haline çevirebilirsin.
Bunun için aşağıdaki komutu çalıştırabilirsin:

bash
Kopyala
Düzenle
pyinstaller --onefile system_info.py
Çevrimiçi dönüştürücülerle .exe oluşturmak istersen şu siteleri kullanabilirsin:

PyInstaller Web
py2exe.net
