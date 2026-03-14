import string

class PasswordTooShortError(Exception):
    """Raised when the password is too short."""
    pass

class PasswordTooCommonError(Exception):
    """Raised when the password consists of only digits, only letters, or only special characters."""
    pass

class PasswordNoSpecialCharactersError(Exception):
    """Raised when the password does not contain at least one special character."""
    pass

class PasswordContainsSpacesError(Exception):
    """Raised when the password contains empty spaces."""
    pass

SPECIAL_CHARACTERS = {"@", "*", "&", "%"}

while True:
    password = input()
    if password == "Done":
        break

    try:
        if len(password) < 8:
            raise PasswordTooShortError("Password must contain at least 8 characters")

        if " " in password:
            raise PasswordContainsSpacesError("Password must not contain empty spaces")

        contains_digit = any(char.isdigit() for char in password)
        contains_letter = any(char.isalpha() for char in password)
        contains_special = any(char in SPECIAL_CHARACTERS for char in password)

        if not contains_special:
            raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

        if not (contains_digit and contains_letter and contains_special):
            raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

        print("Password is valid")

    except (PasswordTooShortError, PasswordTooCommonError, PasswordNoSpecialCharactersError, PasswordContainsSpacesError) as e:
        print(e)
