import argparse
import json
import os

JSON_FILE:str = "mac.json"


def parsejson(file:str) -> dict:
    '''
    A function that returns a dictionary with all the data from the passed json file.
    
    It is better to immediately use a call to some part of the dictionary object. 
    This is due to the fact that objects can be quite large, 
    
    it is recommended to know about their sizes and data in them in advance.
    '''
    text = ''.join(open(file, 'r').readlines())
    return json.loads(text)


class SystemMethods():
    def __init__(self):
        '''
        A class that stores all the methods that 
        can be called during the operation of the application.
        '''

    def openbrowser(self, link):
        os.system(f"xdg-open {link}")
        return
