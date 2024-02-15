import socket

def check_device_availability(host):
    try:
        # Попытка установить соединение с устройством
        socket.create_connection((host, 80), timeout=1)
        print(f"Устройство {host} доступно")
        return True
    except (socket.timeout, socket.error):
        print(f"Устройство {host} недоступно")
        return False

# Замените имена хостов на имена ваших устройств
hosts_to_check = ['sm1532-2-ip5-4.local']

for host in hosts_to_check:
    check_device_availability(host)
