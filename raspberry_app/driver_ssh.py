import paramiko
import pprint
from config import *


def driver(hosts, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    def command_exute(command):
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read().splitlines()
        if result:
            pprint.pprint(result)
            print('OK')

    for host in hosts:
        try:
            ssh.connect(
                    host,
                    PORT,
                    USERNAME,
                    PASSWORD
            )
            command_exute(command)

            # command_exute("reboot")
            # command_exute("export DISPLAY=:0")
            # command_exute("echo 'DISPLAY=:0 chromium-browser https://kompege.ru' | at now")

        except Exception as error:
            print(f'{host}: {error}')



    # stdin, stdout, stderr = ssh.exec_command('reboot')
    # stdin, stdout, stderr = ssh.exec_command('poweroff')
    # stdin, stdout, stderr = ssh.exec_command("export DISPLAY=:0")
    # stdin, stdout, stderr = ssh.exec_command("echo 'DISPLAY=:0 chromium-browser https://site.ru' | at now")
    # result = stdout.read().splitlines()

def driver_sftp(hosts, fname):
    for host in hosts:
        try:
            transport = paramiko.Transport((host, PORT))
            transport.connect(username=USERNAME, password=PASSWORD)
            sftp = paramiko.SFTPClient.from_transport(transport)
            remotepath = f'/home/student/{fname.split('/')[-1]}'
            localpath = fname
            # sftp.get(remotepath, localpath)
            sftp.put(localpath, remotepath)
            sftp.close()
            transport.close()
        except Exception as error:
            print(f'{host}: {error}')