#1
my_dict = {'apple': 10, 'banana': 5, 'cherry': 7}
#Ascending
asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
#Descending
desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Ascending:", asc)
print("Descending:", desc)

#2
d = {0: 10, 1: 20}
d[2] = 30
print("Updated dictionary:", d)

#3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {}
for d in (dic1, dic2, dic3):
    result.update(d)
print("Concatenated dictionary:", result)

#4
n = 5
squares = {x: x*x for x in range(1, n+1)}
print("Squares up to 5:", squares)

#5
squares_15 = {x: x**2 for x in range(1, 16)}
print("Squares from 1 to 15:", squares_15)

#1
my_set = {1, 2, 3}
print("Created set:", my_set)

#2
print("Iterating over set:")
for item in my_set:
    print(item)

#3
my_set.add(4)              # Add one item
my_set.update([5, 6])      # Add multiple items
print("After adding:", my_set)

#4
my_set.remove(1)           # Will raise error if 1 not in set
my_set.discard(10)         # Won't raise error
print("After removing:", my_set)

#5
item_to_remove = 2
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
print("Final set:", my_set)
