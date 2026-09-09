import string
import secrets
def generate_password(length, use_uppercase, use_lowercase,
                      use_numbers, use_symbols):

    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_numbers:
        character_sets.append(string.digits)

    if use_symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        return None

    minimum_required = len(character_sets)

    if length < minimum_required:
        print(
            f"Password length must be at least "
            f"{minimum_required} characters."
        )
        return None

    password_characters = []

    # Guarantee at least one character from each selected category
    for character_set in character_sets:
        password_characters.append(
            secrets.choice(character_set)
        )

    # Combine all selected character sets
    all_characters = "".join(character_sets)

    # Fill remaining positions
    while len(password_characters) < length:
        password_characters.append(
            secrets.choice(all_characters)
        )

    # Secure shuffle
    for i in range(len(password_characters) - 1, 0, -1):

        j = secrets.randbelow(i + 1)

        password_characters[i], password_characters[j] = (
            password_characters[j],
            password_characters[i]
        )

    return "".join(password_characters)
# GET YES / NO INPUT
def yes_no(question):

    while True:

        answer = input(question).strip().lower()

        if answer in ["y", "yes"]:
            return True

        if answer in ["n", "no"]:
            return False

        print("Please enter Y or N.")
def main():

    print("                SECURE PASSWORD GENERATOR")

    while True:

        try:
            length = int(
                input("\nEnter desired password length: ")
            )

            if length <= 0:
                print("Length must be greater than zero.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    print("\nSelect password complexity:")

    uppercase = yes_no(
        "Include uppercase letters? (Y/N): "
    )

    lowercase = yes_no(
        "Include lowercase letters? (Y/N): "
    )

    numbers = yes_no(
        "Include numbers? (Y/N): "
    )

    symbols = yes_no(
        "Include special characters? (Y/N): "
    )

    password = generate_password(
        length,
        uppercase,
        lowercase,
        numbers,
        symbols
    )

    if password is None:
        print("\nUnable to generate password.")
        return

    print("                  GENERATED PASSWORD")
    print(password)
    print("\nPassword generated successfully! 🔐")


if __name__ == "__main__":
    main()