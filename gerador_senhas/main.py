from gerador_senhas.password_generator import *
from user.user_creation import user
from login.login_creation import login


if __name__ == '__main__':
    password = make_password(length=6, chars=False)
    print(password)
    print('--' * 30)
    username = user('Usertest')
    print(username)
    account = login(username, password)
    account2 = login('herik00', make_password(length=12, numbers=False))
    print(account)
    print(account2)
