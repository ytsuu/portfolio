'1'
n = int(input("Введите количество строк: "))
strings = []

for _ in range(n):
    s = input()
    strings.append(s)

print(strings)
'2'
# Генерация списка с заданными элементами
m = [chr(97 + i) * (i + 1) for i in range(26)]

print(m)
'3'
n = int(input("Введите количество чисел: "))
numbers = []

for _ in range(n):
    num = int(input())
    numbers.append(num ** 3)

print(numbers)
'4'
n = int(input("Введите натуральное число: "))
d = []

for i in range(1, n+1):
    if n % i == 0:
        d.append(i)

print(d)
'5'
n = int(input("Введите количество чисел: "))
numbers = []

for _ in range(n):
    num = int(input())
    numbers.append(num)

sums = []
for i in range(n - 1):
    sums.append(numbers[i] + numbers[i+1])

print(sums)

'7'
n = int(input())
numbers = [int(input()) for _ in range(n)]
min_value = min(numbers)
max_value = max(numbers)
numbers.remove(min_value)
numbers.remove(max_value)
for num in numbers:
    print(num)


'8'
text = input()
for word in text.split():
    print(word)


'10'
file_path = input()
parts = file_path.split('\\')
for part in parts:
    print(part)


'11'
numbers = input().split()
for number in numbers:
    print('+' * int(number))


'12'
ip_address = input().split('.')
if all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_address) and len(ip_address) == 4:
    print('ДА')
else:
    print('НЕТ')