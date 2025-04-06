import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    # Define the character pool
    char_pool = string.ascii_lowercase  # Lowercase letters

    if use_uppercase:
        char_pool += string.ascii_uppercase  # uppercase
    if use_numbers:
        char_pool += string.digits  # number
    if use_special:
        char_pool += string.punctuation  # special

    # Make sure the character pool is not empty
    if not char_pool:
        raise ValueError("Select at least one character type")

    # Generate Password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print(" Password Generator")

    # Use predefined input data to prevent input and output errors
    length = 12  # Set password length (12)
    use_uppercase = True  # Confirm have uppercase
    use_numbers = True  # Confirm have number
    use_special = True  # Confirm have special
#可以在上面修改属性
    try:
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"password: {password}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

