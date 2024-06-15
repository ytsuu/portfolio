'5'
def print_digit_sum(num):
    sum_digits = sum(int(digit) for digit in str(num))
    print(sum_digits)

# Пример
num = 12345
print_digit_sum(num)
'4'
def printfio(name, surname, patronymic):
    print(surname, name, patronymic)

# Пример использования функции
name = "Иван"
surname = "Иванов"
patronymic = "Иванович"
printfio(name, surname, patronymic)

'1'
def draw_box():
    for i in range(14):
        if i == 0 or i == 13:
            print("*" * 10)
        else:
            print("*        *")

# Вызов функции
draw_box()

'2'
def draw_triangle():
    for i in range(1, 11):
        print("*" * i)

# Вызов функции
draw_triangle()

'3'
def draw_triangle(fill, base):
    for i in range(1, base+1, 2):
        print((fill*i).center(base))


'6'
def convert_to_miles(km):
    return km * 0.6214
km = float(input("Введите расстояние в километрах: "))
miles = convert_to_miles(km)
print(f"Расстояние в милях: {miles}")


'7'
def get_days(month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month - 1]
month = int(input("Введите номер месяца: "))
days = get_days(month)
print(f"Количество дней в указанном месяце: {days}")


'8'
def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
num = int(input("Введите число: "))
factors = get_factors(num)
print(f"Делители числа {num}: {factors}")


'9'
def number_of_factors(num):
    return len(get_factors(num))
num = int(input("Введите число: "))
count = number_of_factors(num)
print(f"Количество делителей числа {num}: {count}")


'10'
def find_all(target, symbol):
    locations = []
    for i in range(len(target)):
        if target[i] == symbol:
            locations.append(i)
    return locations
target = input("Введите целевую строку: ")
symbol = input("Введите символ для поиска: ")
locations = find_all(target, symbol)
print(f"Позиции символа {symbol} в строке {target}: {locations}")


