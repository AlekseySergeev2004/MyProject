# even_odd.py

def check_even_odd(number):
    """Функция, которая определяет, является ли число четным или нечетным."""
    if number % 2 == 0:
        return "Четное число"
    else:
        return "Нечетное число"

if __name__ == "__main__":
    user_number = int(input("Введите число: "))
    result = check_even_odd(user_number)
    print(f"Введенное число {user_number} - это {result}.")
