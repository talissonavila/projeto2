from user.user_creation import user


def login(username: str, password: str) -> dict:
    password = str(password)
    if len(password) < 4:
        raise ValueError(f'Password must be at least 4. Not {len(password)}.')
    user1 = user(username)
    account = dict()
    account[user1] = password
    return account
