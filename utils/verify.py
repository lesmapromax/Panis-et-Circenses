import re

def verify_password(password: str) -> bool:
    """
    This is a function to make sure the password is a strong password

    The password must be a string

    The password must have 8 characters, an upper and an lower letter, a number and a special symbol
    """
    if len(password) < 8:
        return False

    if not re.search(r'[a-z]+', password):
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[!@#$%&*?]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    return True


