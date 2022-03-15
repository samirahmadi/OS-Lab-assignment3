numbers = []

n=int(input("please enter numbers:\n"))
for i in range(0,n):
 newnumber=int(input())

 numbers.append(newnumber)

print(str(numbers))
x=False
i=1
while i<len(numbers):
    if numbers[i]<numbers[i-1]:
        x=True
    i+=1
if(x==False):
 print( "sorted")
else:
 print("not sorted")