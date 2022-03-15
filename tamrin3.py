import random
numbers = []

n=int(input("please enter numbers:\n"))
for i in range(n):
 number=random.randint(1,100)
 if number not in numbers:
     numbers.append(number)
print(numbers)