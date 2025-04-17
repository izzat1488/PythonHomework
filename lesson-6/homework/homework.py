def modify_string(txt):
    result = ""
    i = 0
    count = 0

    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3:
            if txt[i] not in 'aeiou' and (i + 1 >= len(txt) or txt[i + 1] != '_'):
                result += '_'
                count = 0
            else:
                count = 2

        i += 1

    if result.endswith('_'):
        result = result[:-1]

    return result


def integer_squares(n):
    for i in range(n):
        print(i ** 2)


def print_natural_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1


def print_pattern():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


def sum_upto_number(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    print("Sum is:", total)


def multiplication_table(num):
    for i in range(1, 11):
        print(num * i)


def display_selected_numbers():
    numbers = [12, 75, 150, 180, 145, 525, 50]
    for num in numbers:
        if num > 500:
            break
        if num > 100 and num % 5 == 0:
            print(num)


def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    print("Digits:", count)


def reverse_number_pattern():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


def reverse_list():
    list1 = [10, 20, 30, 40, 50]
    for item in reversed(list1):
        print(item)


def print_negative_range():
    for i in range(-10, 0):
        print(i)


def done_after_loop():
    for i in range(5):
        print(i)
    else:
        print("Done!")


def print_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num)


def fibonacci_series():
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(10):
        print(a, end=' ')
        a, b = b, a + b
    print()


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"{num}! = {fact}")


def uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for key in (c1 - c2):
        result.extend([key] * (c1[key] - c2.get(key, 0)))
    for key in (c2 - c1):
        result.extend([key] * (c2[key] - c1.get(key, 0)))

    return result
