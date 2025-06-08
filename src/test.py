import paramiko

def run_command(hosts, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for host in hosts:
        try:
            print(f"🔹 Подключаемся к {host}...")
            ssh.connect(hostname=host, username=username, password=password, timeout=10)
            
            # Важно: exec_command возвращает (stdin, stdout, stderr)
            stdin, stdout, stderr = ssh.exec_command(command)
            
            # Читаем вывод
            output = stdout.read().decode().strip()
            errors = stderr.read().decode().strip()
            
            if output:
                print(f"✅ {host}: Успех\n{output}")
            if errors:
                print(f"❌ {host}: Ошибки\n{errors}")
                
        except paramiko.SSHException as e:
            print(f"⚠️ SSH-ошибка на {host}: {str(e)}")
        except Exception as e:
            print(f"⚠️ Общая ошибка на {host}: {str(e)}")
        finally:
            ssh.close()

# Пример использования
if __name__ == "__main__":
    HOSTS = ["mp1-b313-l11256", "mp1-b312-l18492"]
    USERNAME = "student"
    PASSWORD = "student"
    COMMAND = "export DISPLAY=:0; DISPLAY=:0 firefox 'https://mos.ru' &"  # Пример команды
    
    run_command(HOSTS, USERNAME, PASSWORD, COMMAND)