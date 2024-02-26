# 
# 
# 
# 

from ping3 import ping
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


def checkDevice(address) -> bool:
    '''
    
    '''
    
    if ping(address):
        return True
    return False


if __name__=="__main__":
    # print(parseData("../data.json"))
    print(checkDevice("server-1"))