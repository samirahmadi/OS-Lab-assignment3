n=int(input("please enter number:\n"))

for i in range(n):
    if i in range(1,n,2):
     print("🟨", end="")
    else:
     print("🟩",end="")