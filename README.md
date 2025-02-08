# 🛠 Sistem Bilgi Toplayıcı (System Info Collector)

### 📌 Açıklama  
Bu Python tabanlı araç, sistemin donanım ve yazılım bilgilerini toplar ve JSON formatında kaydeder.  
Aşağıdaki bilgileri toplar:
- **CPU, RAM, disk** ve **ağ bilgileri**
- **Antivirüs**, **güvenlik duvarı** ve **güncellemeler**
- **Yüklü yazılımlar** ve **çalışan işlemler**
- **USB cihazlar**, **dosya bilgileri**, **IP adresi** ve **sıcaklık sensörü**

Program, gerekli kütüphaneler yüklü değilse, bunları otomatik olarak yükler.

---

### 📦 Kullanılan Kütüphaneler  
Bu araç aşağıdaki Python kütüphanelerini kullanır:
- `psutil`
- `wmi`
- `socket`
- `json`
- `os`
- `platform`
- `time`
- `getpass`
- `subprocess`
- `win32com.client`
- `datetime`

**Not:** Eğer bu kütüphaneler eksikse, program başlatıldığında otomatik olarak yüklenecektir.
