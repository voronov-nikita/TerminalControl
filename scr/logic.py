# 
# The software is provided to automate routine tasks for system administrators, 
# technical specialists, as well as for all those who are engaged in administration, 
# configuration or simple work with multiple devices based on Linux systems.
# 
# All the code from this file is better to use on Windows machines, 
# because the main functions, methods, classes and processes are organized 
# using the console (CMD) capabilities of Windows 10.
# 

from fabric import Connection
import subprocess
import json
import os

HOST:str = "root@192.168.11.185"
PASSWORD:str = "qsc[;."
LIST_IP:list|None = []
COMMAND:str = "ls -la"

# A Path of file with data about the MAC addresses of computers
MAC:str = "mac.json"


class Terminal():
    def __init__(self, host:str, password:str):
        '''
        A class that simulates requests to a terminal over an ssh connection.

        Accepts the arguments necessary to submit the request: 
        
        - `HOST` - a string containing the name of your computer on the network. 
        The login to which the connection will take place and it`s ip address.
        
        - `PASSWORD` - a string containing the password from this user in the system. 
        This password is used when establishing an ssh connection to the computer.
        '''
        
        self.host=host
        self.username = host.split("@")[0]
        self.password = password
        
    
    def run(self, command:str, isPrint:bool=False) -> str:
        '''
        Runs the passed command on behalf of a regular user.
        The command is executed on behalf of the user passed during initialization of the Terminal class object.

        Returns a string with a response from the terminal to which the connection was made. 
        Accordingly, if nothing has come from the terminal, an empty string will be returned

        The `isPrint` argument is needed to understand whether you need a message from the terminal, or you can do without it. 
        If you need it, then pass True as the value for the argument, otherwise do not pass anything or pass False.
        
        '''
        with Connection(self.host, connect_kwargs={"password": self.password}) as connect:
            result = connect.run(command, hide=True)
            if isPrint:
                print(result.stdout.strip())
            return result.stdout.strip()
    
    def runAll(self, command, list_ip, isPrint:bool=False) -> str|tuple:
        '''
        Running a command on multiple machines almost simultaneously. 
        Similar in functionality to the `run()` method. 
        Uses the rights of the user to whom the SSH connection was made.
        
        Accepts as arguments:
        
        - `command` - this is the command that will have to be executed on all 
        machines using the rights of a regular user.
        
        - `list_ip` - list_ip is an array containing the host addresses of 
        all the machines on which the command will be executed. 
        
        It is recommended to pass arguments in the form of an unsigned @ and username. 
        For example , the list may look like this:
        >>> ["192.168.0.11", "192.168.11.14", "192.168.23.211", "192.168.0.14"]

        In this case, the user name will be taken from the host passed during initialization.
        
        '''
        answers = ()
        for ip in list_ip:
            host = str(ip)
            with Connection(host, connect_kwargs={"password": self.password}) as connect:
                result = connect.run(command, hide=True)
                if isPrint:
                    print(f"Answer from {host}:")
                    print(result.stdout.strip() + "\n")
            answers = answers + (result.stdout.strip(),)
        return answers
            
                
    def sendFile(self, filepath:str, receiverhost:str, dir:str="/home") -> str:
        '''
        
        '''
        command = f"scp {filepath} {receiverhost}:{dir}".split()
        com = subprocess.check_output(list(command), shell=True)
        print(com)
        return com.decode()
    
    def sendFileAll(self, filepath:str, list_ip:list, dir:str="/home") -> str:
        '''
        Send the file to many computers.
        '''
        statuss = tuple()
        for host in list_ip:
            command = f"scp {filepath} {host}:{dir}".split()
            com = subprocess.check_output(command, shell=True)
            statuss = statuss + (com.decode(), )
        
        return statuss

def network_scan(serchRange:str) -> dict:
    '''
    Executes a command to fill in the arp table relative to the 
    ip address of the user who is making the request.
    
    The search Range argument should be passed as 
    >>> network_scan('192.168.0.1')
    
    Returns a dictionary where the key will be the MAC a
    ddresses of the found computers, 
    and the value is the IP address of the found device.
    
    '''
    
    result = dict()
    
    networkrange = '.'.join(serchRange.split(".")[:-1])
    os.system(rf"for /L %a in (1,1,254) do @start /b ping {networkrange}.%a -n 2 > nul")

    string = subprocess.run(['arp', '-a'], shell=True, capture_output=True, text=True).stdout.split("\n")
    for elem in string:
        timels = elem.split()
        if "192." not in elem:
            continue
        result[timels[1].replace("-", ":")] = timels[0]

    return result


def check_ip(number:int, zone:int) -> dict | None:
    macfile = open(MAC, 'r')
    jsondata = json.load(macfile)
    networkdata = network_scan("192.168.0.1")
    try:
        return networkdata[jsondata[f"Zone{zone}"][str(number)]]
    except KeyError:
        return None
    

if __name__=="__main__":
    term = Terminal(HOST, PASSWORD)
    # term.sendFileAll("mac.json", LIST_IP, "/home/vnr")
    # term.runAll(COMMAND, LIST_IP, isPrint=True)
    term.run(COMMAND, isPrint=True)