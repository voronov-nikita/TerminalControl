import paramiko

# Создаем объект SSHClient
ssh = paramiko.SSHClient()

# Устанавливаем политику подтверждения ключей
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Подключаемся к удаленному серверу
ssh.connect('192.168.0.24', username='student', password='qsc[;.')

# Выполняем команду с sudo
command_with_sudo = 'export DISPLAY=:0'
stdin, stdout, stderr = ssh.exec_command(command_with_sudo)

# Вводим пароль для sudo
# stdin.write('qsc[;.\n')
# stdin.flush()

# Читаем результат выполнения команды
result = stdout.read().decode('utf-8')
print(result)

# Закрываем соединение
ssh.close()
