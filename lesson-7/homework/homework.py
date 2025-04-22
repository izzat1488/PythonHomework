#task1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#task2
def digit_sum(k):
    return sum(int(digit) for digit in str(k))
#task3
def powers_of_two(N):
    result = []
    power = 1
    while (value := 2 ** power) <= N:
        result.append(value)
        power += 1
    print(*result)
