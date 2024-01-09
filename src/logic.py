# 
# 
# 
# 


import paramiko
import json
import os


# 
class Actions():
    def __init__(self, user:str, host:str, password:str) -> None:
        self.user = user
        self.host = host
        self.password = password
        
    
    def connect(self) -> None:
        '''
        
        '''
        
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.ssh.connect(self.host, username=self.user, password=self.password)
        
    def exportDisplay(self) -> None:
        '''
        
        '''
        
        self.ssh.exec_command("export DISPLAY=:0")
    
    def remotePrint(self, command:str) -> str:
        '''
        
        '''
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read().decode('utf-8')
    
    def executeCommand(self, command:str, sudoPassword:str=None, output:bool=False) -> str|None:
        '''
        
        '''
        
        if sudoPassword is not None:
            stdin, stdout, stderr = self.ssh.exec_command(command, get_pty=True)
            stdin.write(sudoPassword+"\n")
            stdin.flush()
        else:
            stdin, stdout, stderr = self.ssh.exec_command(command)
        
        if output:
            return stdout.read().decode('utf-8')
        return 
    

# 
class SpecialAction(Actions):
    def __init__(self, user, host, password):
        
        super().__init__(user, host, password)
        
        self.connect()
        self.exportDisplay()
        
    def openWebBrowser(self, url:str) -> None:
        '''
        
        '''
        
        self.executeCommand(f"setsid chromium-browser {url}")
        
    def turnOff(self) -> None:
        '''
        
        '''
        
        self.executeCommand("poweroff")
        
    def reboot(self, sudoPassword:str) -> None:
        '''
        
        '''
        
        self.executeCommand(f"sudo reboot", sudoPassword=sudoPassword)
        
    def sendFile(self, localFilePath:str, remoteFilePath:str) -> None:
        '''
        
        '''
        
        scp = self.ssh.open_sftp()
        scp.put(localFilePath, remoteFilePath)
        scp.close()
        
    def WakeOnLan(self, macAdress:str) -> None:
        '''
        
        '''
        
        os.system(f"wakeonlan {macAdress}")



def parseData(file:str) -> dict:
    '''
    
    '''
    data = open(file, "r")
    return json.load(data)