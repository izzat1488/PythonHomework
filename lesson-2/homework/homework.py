#task1
 
 name = input("Enter your name: ")
 year_of_birth = int(input("Enter your year of birth: "))
 current_year = 2025
 age = current_year - year_of_birth
 print(f"Hello {name}, you are {age} years old.")
 
 #task2
  
   txt = 'LMaasleitbtui'
 
 car1 = txt[0:11:2] 
 car2 = txt[1:11:2] 
 print("Cars:", car1, "and", car2)
 
 #task3
   
   txt = 'MsaatmiazD'
 
 car1 = txt[::2] 
 car2 = txt[1::2]  
 print("Cars:", car1, "and", car2)
 
 #task4
 
 txt = "I'am John. I am from London"
 area = txt.split("from ")[-1]
 print("Residence area:", area)
 
 
 #task5
 
 
 text = input("Enter a string: ")
 reversed_text = text[::-1]
 print("Reversed string:", reversed_text)
 
 
 #task6
 
 
 text = input("Enter a string: ")
 vowels = "aeiouAEIOU"
 count = sum(1 for char in text if char in vowels)
 print("Number of vowels:", count)
 
 #task7
 
 
 
 numbers = input("Enter numbers separated by space: ")
 num_list = [int(n) for n in numbers.split()]
 print("Maximum value:", max(num_list))
 
 #task8
 
 
 
 word = input("Enter a word: ")
 if word == word[::-1]:
     print("It's a palindrome.")
 else:
     print("It's not a palindrome.")
 
 #task9
 
 
 email = input("Enter your email: ")
 domain = email.split('@')[-1]
 print("Email domain:", domain)
 
 #task10
 
 
 import random
 import string
 
 length = 12
 characters = string.ascii_letters + string.digits + string.punctuation
 password = ''.join(random.choice(characters) for _ in range(length))
 print("Generated password:", password)
