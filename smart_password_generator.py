import string
import secrets


def get_strength_label(password: str) -> str:
    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    variety_count = sum([has_lower, has_upper, has_digit, has_symbol])

    # Simple scoring rule:
    # - Weak: length < 8 or variety_count <= 1
    # - Medium: length >= 8 and variety_count == 2 or 3
    # - Strong: length >= 12 and variety_count == 4
    if length < 8 or variety_count <= 1:
        return "Weak"
    elif length >= 12 and variety_count == 4:
        return "Strong"
    else:
        return "Medium"


def generate_password(length=12,
                      use_lower=True,
                      use_upper=True,
                      use_digits=True,
                      use_symbols=True):
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if not characters:
        raise ValueError("At least one character type must be selected.")

    if length < 4:
        raise ValueError("Length should be at least 4 for a strong password.")

    password_chars = []

    if use_lower:
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_upper:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        password_chars.append(secrets.choice(string.digits))
    if use_symbols:
        password_chars.append(secrets.choice("!@#$%^&*()-_=+[]{}|;:,.<>?/"))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def ask_bool(prompt: str) -> bool:
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please enter y or n.")


def main():
    print("=== Smart Password Generator ===")

    while True:
        try:
            length = int(input("Enter password length (e.g. 12): ").strip())
            if length <= 0:
                print("Length must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_lower = ask_bool("Include lowercase letters (a-z)?")
    use_upper = ask_bool("Include uppercase letters (A-Z)?")
    use_digits = ask_bool("Include digits (0-9)?")
    use_symbols = ask_bool("Include symbols (!@#$...)?")

    try:
        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
        strength = get_strength_label(password)

        print("\nYour generated password:")
        print(password)
        print(f"\nStrength: {strength}")
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
