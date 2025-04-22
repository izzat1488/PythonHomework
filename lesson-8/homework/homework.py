

# 1
try:
    num = int(input("Введите число: "))
    result = num / 0
except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно!")

# 2
try:
    num = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка: Это не целое число!")

# 3
try:
    with open("somefile.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Ошибка: Файл не найден!")

# 4
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
except ValueError:
    raise TypeError("Ошибка: Ввод должен быть числовым!")

# 5
try:
    with open("/etc/shadow", "r") as file:
        print(file.read())
except PermissionError:
    print("Ошибка: Нет прав доступа к файлу!")

# 6
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Ошибка: Индекс вне диапазона списка!")

# 7
try:
    num = input("Введите число: ")
except KeyboardInterrupt:
    print("\nВвод отменён пользователем.")

# 8
try:
    a = 10
    b = 0
    print(a / b)
except ArithmeticError as e:
    print("Арифметическая ошибка:", e)

# 9
try:
    with open("file.txt", encoding="ascii") as file:
        print(file.read())
except UnicodeDecodeError:
    print("Ошибка: Проблема с кодировкой при чтении файла.")

# 10
my_list = [1, 2, 3]
try:
    my_list.upper()
except AttributeError:
    print("Ошибка: Объект не имеет данного атрибута.")




# 1. 
with open("sample.txt", "r") as f:
    print(f.read())

# 2
n = 3
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

# 3
with open("sample.txt", "a") as f:
    f.write("\nНовая строка")
with open("sample.txt", "r") as f:
    print(f.read())

# 4
from collections import deque
n = 2
with open("sample.txt") as f:
    last_lines = deque(f, maxlen=n)
    for line in last_lines:
        print(line, end="")

# 5
with open("sample.txt") as f:
    lines = f.readlines()
print(lines)

# 6
with open("sample.txt") as f:
    content = f.read()
print(content)

# 7
with open("sample.txt") as f:
    array = [line.strip() for line in f]
print(array)

# 8
with open("sample.txt") as f:
    words = f.read().split()
    longest = max(words, key=len)
    print(longest)

# 9
with open("sample.txt") as f:
    line_count = sum(1 for _ in f)
    print(line_count)

# 10
from collections import Counter
with open("sample.txt") as f:
    word_freq = Counter(f.read().replace(",", "").split())
    print(word_freq)

# 11
import os
print(os.path.getsize("sample.txt"))

# 12
items = ["яблоко", "банан", "груша"]
with open("output.txt", "w") as f:
    for item in items:
        f.write(item + "\n")

# 13
with open("sample.txt", "r") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())

# 14
with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

# 15
import random
with open("sample.txt") as f:
    print(random.choice(f.readlines()).strip())

# 16
f = open("sample.txt")
print(f.closed)  # False
f.close()
print(f.closed)  # True

# 17
with open("sample.txt") as f:
    clean_lines = [line.strip() for line in f]
print(clean_lines)

# 18
with open("sample.txt") as f:
    words = f.read().replace(",", "").split()
    print("Количество слов:", len(words))

# 19
files = ["file1.txt", "file2.txt"]
chars = []
for filename in files:
    with open(filename) as f:
        chars.extend(list(f.read()))
print(chars)

# 20
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"Файл {letter}\n")

# 21
n = 5
alphabet = string.ascii_uppercase
with open("alphabet.txt", "w") as f:
    for i in range(0, len(alphabet), n):
        f.write(alphabet[i:i+n] + "\n")
