import os
import authorization
from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    if os.path.exists("key.hey"):
        with open('key.key', 'wb') as key_file:
            key_file.write(key)


def load_key():
    with open("key.key", "r") as f:
        key = f.read()
    return key


def add(cipher):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    encrypted_password = cipher.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as file:
        file.write(f"{login}|{encrypted_password}\n")


def view(cipher):
    with open("passwords.txt", "r") as f:
        for line in f:
            line = line.strip()
            login, encrypted_password = line.split('|')
            decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
            print(f"Логин: {login} | Пароль: {decrypted_password}")


def main():
    write_key()
    key = load_key()
    cipher = Fernet(key)
    while True:
        choice = input("1. Посмотреть, 2. Добавить, 3. Выйти ")
        if choice == "1":
            view(cipher)
        elif choice == "2":
            add(cipher)
        elif choice == "3":
            break


if __name__ == "__main__":
    main()