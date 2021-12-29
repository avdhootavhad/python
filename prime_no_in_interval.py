a = int(input("Enter the Starting element "))
b = int(input("Enter last element "))
for num in range (a, b+1):
    for x in range (2,num):
        if num%x==0:
            break
    else:
        print(num)

