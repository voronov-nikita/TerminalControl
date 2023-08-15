from cryptography.fernet import Fernet

# Генерируем ключ
key = Fernet.generate_key()

# Создаем объект Fernet с использованием ключа
cipher_suite = Fernet(key)

# Строка, которую хотим зашифровать
original_string = "То, что нужно зашифровать!"

# Шифруем строку
encrypted_string = cipher_suite.encrypt(original_string.encode())

print("Зашифрованная строка:", encrypted_string)

# Расшифровываем строку
decrypted_string = cipher_suite.decrypt(encrypted_string).decode()

print("Расшифрованная строка:", decrypted_string)

