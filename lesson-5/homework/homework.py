#1
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#2
def check_weird(n):
    """
    Prints whether the number is 'Weird' or 'Not Weird' based on conditions.
    """
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:  # n > 20
        print("Not Weird")


#3

a = 4
b = 12


start = a if a % 2 == 0 else a + 1
if start > b:
    even_numbers_1 = []
else:
    even_numbers_1 = list(range(start, b + 1, 2))

print("\nEven numbers (solution 1 with if-else):", even_numbers_1)

