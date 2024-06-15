'1'
s = input("Введите строку: ")

for c in reversed(s):
    print(c)
'2'
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
patronymic = input("Введите отчество: ")

initials = name[0].upper() + '.' + surname[0].upper() + '.' + patronymic[0].upper() + '.'
print(initials)
'4'
s = input("Введите строку: ")

p = s.count("+")
s = s.count("*")

print(f"Символ '+' встречается {count_p} раз")
print(f"Символ '*' встречается {count_s} раз")

'6'
d = int(input("Введите натуральное число: "))
b = bin(d)[2:]

print(f"Двоичное представление числа {d}: {b}")

'10'
s = input()
name, surname = s.split()

if name0.isupper() and surname0.isupper():
    print("Верно")
else:
    print("Неверно")

'5'
string = input()
swapped_case_string = string.swapcase()
print(swapped_case_string)

'7'
string = input()
lowercase_count = sum(1 for char in string if char.islower())
print("Количество буквенных символов в нижнем регистре:", lowercase_count)

'12'
string = input()
first_index = string.find('h')
last_index = string.rfind('h')
result = string[:first_index] + string[last_index+1:]
print(result)


'13'
string = input()
char_count = {}
for char in string:
    if char.isalpha():
        char_count[char] = char_count.get(char, 0) + 1
most_frequent_char = max(char_count, key=char_count.get)
print(most_frequent_char)


'14'
string = input()
first_index = string.find('f')
last_index = string.rfind('f')
if first_index == -1:
    print("NO")
elif first_index == last_index:
    print(first_index)
else:
    print(first_index, last_index)





