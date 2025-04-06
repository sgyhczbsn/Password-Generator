import random
import string


def generate_password(length, use_uppercase, use_numbers, use_special):
    # 定义字符池
    char_pool = string.ascii_lowercase  # 小写字母

    if use_uppercase:
        char_pool += string.ascii_uppercase  # 大写字母
    if use_numbers:
        char_pool += string.digits  # 数字
    if use_special:
        char_pool += string.punctuation  # 特殊字符

    if not char_pool:
        raise ValueError("Select at least one character type")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " (Y/N): ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print(" Y or N。")


def main():
    print("Password Generator")

    try:
        length = int(input("请输入密码长度Please enter the password length（such as 12）: "))
        if length <= 0:
            raise ValueError("长度必须为正整数Please enter an integer")

        use_uppercase = ask_yes_no("是否包含大写字母(uppercase letters?)")
        use_numbers = ask_yes_no("是否包含数字(number)?")
        use_special = ask_yes_no("是否包含特殊字符(Special characters)?")

        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"\n password is：{password}")

    except ValueError as ve:
        print(f"Input Error：{ve}")
    except Exception as e:
        print(f"An exception occurred：{e}")


if __name__ == "__main__":
    main()
