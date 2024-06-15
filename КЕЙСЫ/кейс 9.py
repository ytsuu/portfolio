# №1
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
last = (countries[-1])

print("№1")
print(last)

# №2
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)

print("№2")
print(primes[:7])

# №3
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')

print("№3")
print(countries[2:])

# №4
print("№4")
print((countries[:-3]))

# №5
print("№5")
print((countries[2:-2]))

# №6
countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
number = len(countries)

print("№6")
print(number)

# №7
numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)

print("№7")
print(min(numbers) + max(numbers))

# №8
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
index = countries.index('Slovenia')

print("№8")
print(index)

# №9
countries = (
    'Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain',
    'Cameroon')
number = countries.count('Spain')

print("№9")
print(number)

# №10
numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)

print("№10")
print(numbers1 * 2 + numbers2 * 9 + numbers3)

# №11
city_name = input("Введите название города")
city_year = int(input("Введите год основания города"))
city = city_name, city_year

print("№11")
print(city)

# №12
# Дополните приведенный код, так чтобы получить список, содержащий только непустые кортежи исходного списка tuples, не меняя порядка их следования.
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i]

print("№12")
print(non_empty_tuples)

# №13
# Дополните приведенный код так, чтобы переменная new_tuples содержала список кортежей на основе списка tuples с последним элементом каждого кортежа, замененным на численное значение 100.
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [i[:-1] + (100,) for i in tuples]

print("№13")
print(new_tuples)

# №14
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
composition = 1
for i in (numbers):
    composition *= i

print("№14")
print(composition)

# №15
data = 'Python для продвинутых!'
print("№15")
print(tuple(data))

# №16
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
real_poet = []

for i in poet_data:
    if i == poet_data[-1]:
        new_poet = "москва"
    else:
        new_poet = i
    real_poet.append(new_poet)
real_poet = tuple(real_poet)

print("№16")
print(real_poet)

# №17
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
print("№17")
for i in numbers:
    arithmetic_mean = sum(i) / len(i)
    print(arithmetic_mean)

# № вершина параболы
print("№ вершина параболы")
a = int(input("введите а"))
b = int(input("введите b"))
c = int(input("введите c"))

x = -b / (2 * a)
y = 4 * a * c - (b ** 2) / (4 * a)

print(f"{x}, {y}")

# № конкурсный отбор
print(("№конкурсный отбор"))
num_students = int(input("Введите количество студентов: "))

students_data = []
for i in range(num_students):
    student = input("Введите имя студента и его оценку: ")
    students_data.append(student)

for student in students_data:
    print(student)

print()

for student in students_data:
    if int(student.split()[1]) >= 4:
        print(student)

# трибоначи
print("№последовательность трибоначчи")
n = int(input("Введите количество чисел последовательности Трибоначчи, которые вы хотите получить: "))

tribonacci_sequence = [1, 1, 1]

while len(tribonacci_sequence) < n:
    tribonacci_sequence.append(sum(tribonacci_sequence[-3:]))

for i in range(n):
    print(tribonacci_sequence[i], end=' ')