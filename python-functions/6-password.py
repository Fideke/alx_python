def validate_password(password):
    if len(password) < 0:
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    elif not any(char.isdigit() for char in password):
        return False