def user(username: str) -> str:
    if not isinstance(username, str):
        raise TypeError(f'User param must be string. Not {type(username)}.')
    if len(username) < 4:
        raise ValueError(f'User must be at least 4. Not {len(username)}.')
    return username
