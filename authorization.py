from main import load_key
from cryptography.fernet import Fernet


def authorization(login, password, cipher):
    with open("passwords.txt", "r") as f:
        for line in f:
            line = line.strip()
            stored_login, encrypted_password = line.split('|')
            decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
            if login == stored_login and password == decrypted_password:
                return True
        return False


def main():
    key = load_key()
    cipher = Fernet(key)
    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if authorization(login, password, cipher):
            print("вы авторизированны")
            break
        else:
            print("такого пользователя нет")


if __name__ == "__main__":
    main()