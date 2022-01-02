#https://www.codesansar.com/python-programming-examples/print-54321-5432-543-54-5-pattern.html

# reversed oredered 54321
n = int(input("Enter number : "))
for i in range(1,n+1):
    for j in range(n, i-1,-1):
        print(j,end=" ")
    print()
'''n = int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(1, i+1,):
        print(j,end=" ")
    print()'''

