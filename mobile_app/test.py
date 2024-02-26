import threading
from ping3 import ping

def checkDevice(address) -> bool:
    '''
    Ваша реализация функции ping
    '''
    if ping(address):
        return True
    return False

def check_devices_parallel(addresses):
    results = []

    def worker(address):
        result = checkDevice(address)
        results.append(result)

    # Создаем и запускаем потоки для каждого адреса
    threads = [threading.Thread(target=worker, args=(address,)) for address in addresses]
    for thread in threads:
        thread.start()

    # Дожидаемся завершения всех потоков
    for thread in threads:
        thread.join()

    return results

# Пример использования
addresses_to_check = ['192.168.0.1', '192.168.0.10', '192.168.1.3']
results = check_devices_parallel(addresses_to_check)

# Результаты будут содержать True или False в зависимости от того, доступен ли каждый хост
print(results)
