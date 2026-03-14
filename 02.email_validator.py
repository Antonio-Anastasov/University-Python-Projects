class NameTooShortError(Exception):
    """Raised when the name in the email is too short."""
    pass

class MustContainAtSymbolError(Exception):
    """Raised when the email does not contain '@'."""
    pass

class InvalidDomainError(Exception):
    """Raised when the domain is invalid."""
    pass

VALID_DOMAINS = {".com", ".bg", ".net", ".org"}

while True:
    email = input()
    if email == "End":
        break

    try:
        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain @")

        name, domain_part = email.split("@", 1)

        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        domain = "." + domain_part.split(".")[-1]
        if domain not in VALID_DOMAINS:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        print("Email is valid")

    except (NameTooShortError, MustContainAtSymbolError, InvalidDomainError) as e:
        print(e)
