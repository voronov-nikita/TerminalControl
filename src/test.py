
from ping3 import ping

def check_device_online(ip_address):
    # Выполняем ICMP ping на устройство
    if ping(ip_address):
        print(f"Устройство с IP-адресом {ip_address} доступно в сети.")
    else:
        print(f"Устройство с IP-адресом {ip_address} не доступно в сети.")
