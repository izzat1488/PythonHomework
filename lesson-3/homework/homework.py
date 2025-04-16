#1
fruits = ["apple", "banana", "cherry", "orange", "mango"]
print("Third fruit:", fruits[2])  

#2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Concatenated list:", combined_list)

#3
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("Extracted elements:", new_list)

#4
favorite_movies = ["Inception", "Interstellar", "Matrix", "Gladiator", "Titanic"]
movies_tuple = tuple(favorite_movies)
print("Movies as tuple:", movies_tuple)

#5
cities = ["London", "Paris", "Rome", "Berlin"]
print("Is Paris in the list?", "Paris" in cities)

#6
original = [1, 2, 3]
duplicated = original * 2
print("Duplicated list:", duplicated)

#7
nums = [1, 2, 3, 4, 5]
nums[0], nums[-1] = nums[-1], nums[0]
print("Swapped list:", nums)

#8
numbers_tuple = tuple(range(1, 11))
print("Tuple slice (index 3 to 7):", numbers_tuple[3:8])

#9
colors = ["blue", "red", "blue", "green", "blue"]
count_blue = colors.count("blue")
print("Count of 'blue':", count_blue)

#10
animals = ("cat", "dog", "lion", "tiger")
lion_index = animals.index("lion")
print("Index of 'lion':", lion_index)

#11
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)

#12
my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))

#13
number_tuple = (100, 200, 300, 400, 500)
number_list = list(number_tuple)
print("Tuple converted to list:", number_list)

#14
num_tuple = (9, 2, 5, 11, 7)
print("Max:", max(num_tuple))
print("Min:", min(num_tuple))

#15
words = ("hello", "world", "python", "rocks")
reversed_words = words[::-1]
print("Reversed tuple:", reversed_words)
