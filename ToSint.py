import psutil
import wmi
import socket
import json
import os
import platform
import time
import getpass
import subprocess
import subprocess
import sys
import win32com.client
from datetime import datetime

libraries = [
    "psutil", "wmi", "socket", "json", "os", "platform", "time", 
    "getpass", "subprocess", "pywin32"
]

# Eksik kütüphaneleri kontrol et
missing_libraries = [lib for lib in libraries if not __import__("importlib").util.find_spec(lib)]

if missing_libraries:
    print(f"[*] Eksik kütüphaneler bulundu: {', '.join(missing_libraries)}")
    print("[*] Eksik kütüphaneler yükleniyor...")
    for lib in missing_libraries:
        subprocess.call([sys.executable, "-m", "pip", "install", lib])
    print("[+] Eksik kütüphaneler yüklendi, devam ediliyor...\n")
else:
    print("[+] Tüm kütüphaneler yüklü, devam ediliyor...\n")

# Sistem bilgilerini al
def get_system_info():
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture(),
        "hostname": platform.node(),
        "cpu": get_cpu_info(),
        "ram": get_ram_info(),
        "disk": get_disk_info(),
        "network": get_network_info(),
        "user": get_user_info(),
        "antivirus": get_antivirus_info(),
        "usb_devices": get_usb_devices(),
        "processes": get_processes_info(),
        "files": get_files_info(),
        "ip_address": get_ip_address(),
        "public_ip": get_public_ip(),
        "firewall": get_firewall_status(),
        "updates": get_update_info(),
        "temperature": get_temperature_info(),
        "backup": get_backup_info(),
        "installed_software": get_installed_software()
    }
    return system_info

# CPU bilgisi al
def get_cpu_info():
    cpu_info = {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "cpu_usage_percent": psutil.cpu_percent(interval=1)
    }
    return cpu_info

# RAM bilgisi al
def get_ram_info():
    ram = psutil.virtual_memory()
    ram_info = {
        "total": ram.total,
        "available": ram.available,
        "percent": ram.percent,
        "used": ram.used,
        "free": ram.free
    }
    return ram_info

# Disk bilgisi al
def get_disk_info():
    disk_info = []
    for partition in psutil.disk_partitions():
        partition_info = {}
        partition_info["device"] = partition.device
        partition_info["mountpoint"] = partition.mountpoint
        partition_info["fstype"] = partition.fstype
        partition_info["opts"] = partition.opts
        usage = psutil.disk_usage(partition.mountpoint)
        partition_info["usage"] = {
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
            "percent": usage.percent
        }
        disk_info.append(partition_info)
    return disk_info

# Ağ bilgisi al
def get_network_info():
    network_info = {}
    addrs = psutil.net_if_addrs()
    for interface, addrs_list in addrs.items():
        for addr in addrs_list:
            if addr.family == socket.AF_INET:
                network_info[interface] = addr.address
    return network_info

# Kullanıcı bilgisi al
def get_user_info():
    user_info = {
        "username": getpass.getuser(),
        "user_home": os.path.expanduser("~")
    }
    return user_info

# Antivirüs bilgisi al (Alternatif yöntem)
def get_antivirus_info():
    """Antivirüs yazılımı durumu"""
    antivirus_info = {}
    try:
        # Windows antivirüs bilgisi (Windows Defender)
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        wmi_service = wmi.ConnectServer(".", "root\\SecurityCenter2")
        query = "SELECT * FROM AntiVirusProduct"
        items = wmi_service.ExecQuery(query)
        for item in items:
            antivirus_info = {
                "name": item.displayName,
                "state": item.productState
            }
    except Exception as e:
        antivirus_info = {"error": f"Antivirüs bilgisi alınamadı: {e}"}
    return antivirus_info

# USB cihazlarını al
def get_usb_devices():
    c = wmi.WMI()
    usb_devices = []
    for usb in c.query("SELECT * FROM Win32_USBHub"):
        usb_devices.append(usb.DeviceID)
    return usb_devices

# Çalışan işlemleri al
def get_processes_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_info']):
        process_info = {
            "pid": proc.info['pid'],
            "name": proc.info['name'],
            "status": proc.info['status'],
            "cpu_percent": proc.info['cpu_percent'],
            "memory_usage": proc.info['memory_info'].rss
        }
        processes.append(process_info)
    return processes

# Dosya bilgilerini al
def get_files_info(directory="C:\\"):  # Varsayılan olarak C: dizinini alır
    files_info = []
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_info = {
                    "file_name": file,
                    "file_path": file_path,
                    "file_size": os.path.getsize(file_path),
                    "created_time": os.path.getctime(file_path),
                    "modified_time": os.path.getmtime(file_path)
                }
                files_info.append(file_info)
    except Exception as e:
        return f"Dosya bilgisi alınamadı: {str(e)}"
    return files_info

# Güvenlik Duvarı Durumu
def get_firewall_status():
    try:
        firewall = subprocess.check_output(["netsh", "advfirewall", "show", "allprofiles"]).decode()
        if "State" in firewall and "ON" in firewall:
            return "Firewall: ON"
        else:
            return "Firewall: OFF"
    except subprocess.CalledProcessError:
        return "Firewall bilgisi alınamadı"

# Sistem Güncellemeleri Bilgisi
def get_update_info():
    try:
        updates = subprocess.check_output(["powershell", "-Command", "Get-WindowsUpdate"]).decode()
        return updates.strip() if updates else "Güncellemeler mevcut değil."
    except subprocess.CalledProcessError:
        return "Güncellemeler bilgisi alınamadı"

# Sıcaklık Sensör Bilgisi
def get_temperature_info():
    try:
        temperature = psutil.sensors_temperatures()
        if 'coretemp' in temperature:
            return temperature['coretemp']
        else:
            return "Sıcaklık bilgisi alınamadı."
    except Exception as e:
        return str(e)

# Yedekleme Yazılımı Bilgisi
def get_backup_info():
    # Yedekleme yazılımı kontrolü yapılabilir. Şu an için basit bir kontrol yapılmakta.
    return "Yedekleme yazılımı bilgisi alınamadı."

# Yüklü Yazılımlar
def get_installed_software():
    installed_software = []
    try:
        software_list = subprocess.check_output(["wmic", "product", "get", "name"]).decode()
        installed_software = software_list.splitlines()[1:]  # Başlık satırını çıkar
    except subprocess.CalledProcessError:
        return "Yazılım bilgisi alınamadı."
    return installed_software

# IP adresini al
def get_ip_address():
    ip_address = None
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
    except socket.error:
        pass
    return ip_address

# Public IP adresini al
def get_public_ip():
    public_ip = None
    try:
        public_ip = subprocess.check_output(["curl", "ifconfig.me"]).decode().strip()
    except subprocess.CalledProcessError:
        pass
    return public_ip

# Verileri JSON formatında kaydet
def save_to_json(data, filename='system_info.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    system_info = get_system_info()
    save_to_json(system_info)
    print("Sistem bilgileri başarıyla kaydedildi.")
