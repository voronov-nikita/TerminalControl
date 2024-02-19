# 
# 
# 
# 

import json


def parseData(file: str) -> dict:
    '''
    Функция парсинга данных.
    
    Функция нужна чтобы считать все данные с data.json и записать его содержание
    в переменную типа словаря.
    '''

    data = open(file, "r")
    return json.load(data)


if __name__=="__main__":
    print(parseData("../data.json"))