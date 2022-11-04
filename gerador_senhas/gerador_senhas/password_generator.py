from random import randint, choice, shuffle


def make_one_special_char() -> str:
    """Creates a special char, choosing one of four unicode ranges.

    Args:
        None.

    Returns:
        chr(choice(char_ranges))chr(choice(char_ranges)) (str): one special char.
    """
    char_ranges = [
        randint(32, 47),
        randint(58, 64),
        randint(91, 96),
        randint(123, 126),
    ]
    return chr(choice(char_ranges))


def make_one_uppercase_letter() -> str:
    """Creates a char in uppercase letter. Range: A-Z.

    Args:
        None.

    Returns:
         chr(randint(65, 90)) (str): one uppercase letter.
    """
    return chr(randint(65, 90))


def make_one_lowercase_letter() -> str:
    """Creates a char in lowercase letter. Range: a-z.

    Args:
        None.

    Returns:
         chr(randint(97, 122)) (str): one lowercase letter.
    """
    return chr(randint(97, 122))


def make_one_number() -> str:
    """Creates a char in number. Range: 0-9.

    Args:
        None.

    Returns:
         chr(randint(48, 57)) (str): one number in range 0, 9.
    """
    return chr(randint(48, 57))


def make_password(length: int = 16, chars: bool = True, lower: bool = True, upper: bool = True,
                  numbers: bool = True) -> str:
    """Creates a passowrd with at least 4 chars. If length was not declared. Passoword has length of 16.
    Password must have: special chars or lowercase letter or uppercase letter or numbers.

    Args:
        length (int): the length of password. If not declared, it will be length of 16.
        chars (bool): if the password has or hasn't special chars.
        lower (bool): if the password has or hasn't lowercase letters.
        upper (bool): if the password has or hasn't uppercase letters.
        numbers (bool): if the passowrd has or hasn't numbers.

    Retuns:
        ''.join(new_password) (str): the password complete.
    """
    if not isinstance(length, int):
        raise TypeError(f'Password length must be integer.')

    if length < 4:
        raise ValueError(f'Password must be at least 4. Not {length}.')

    if not chars and not lower and not upper and not numbers:
        raise TypeError('At least one param must be true')

    new_password = []
    for count in range(length - 1):
        chars and new_password.append(make_one_special_char())
        lower and new_password.append(make_one_lowercase_letter())
        upper and new_password.append(make_one_uppercase_letter())
        numbers and new_password.append(make_one_number())

    new_password = new_password[0:length]
    shuffle(new_password)
    return ''.join(new_password)
