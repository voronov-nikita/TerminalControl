#
#
#
#

from ping3 import ping
from wakeonlan import send_magic_packet
import asyncio
import json


def parseData(file: str) -> dict:
    '''
    Функция парсинга данных.

    Функция нужна чтобы считать все данные с data.json и записать его содержание
    в переменную типа словаря.
    '''

    data = open(file, "r")
    return json.load(data)


def checkDevice(address: str) -> bool:
    '''
    Функция, проверяющая досутпность компьютера в локальной сети.

    Функция работает через библиотеку ```ping3``` и использует ping запрос на компьютер
    и проверяет есть ли соединение. В случае если соединение есть, то функция вернет True, иначе False.

    Используется для подтверждения подключения и ускорения подлючения, путем обхода недоступных компьютеров.

    '''

    if ping(address):
        return True
    return False


def WakeOnLan(macAddress: str) -> None:
    '''
    Включить по сети.

    Если компьютер подключен к локальной сети по беспроводному соединению, то 
    скорее всего ему доспно включение по сети.

    Это работает таким образом, чтобы по mac адресу узнать индификаор компьютера 
    и отправить ему магический пакет, который как раз его и разбудит.

    '''

    try:
        # отправляем запрос дважды для подтверждения получения пакета
        send_magic_packet(macAddress)
        print(f"Magic packet sent to {macAddress}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    ls = parseData("../data.json")["zones"]['zone3']
    
    for i in ls.keys():
        print(ls[i]['mac'])
        mac = ls[i]['mac']
        WakeOnLan(mac)
