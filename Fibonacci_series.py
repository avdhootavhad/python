nthterm = int(input("Enter Number "))
#here we have defined 1st two terms of Fibonacci series
n1=0
n2=1
#used count to compare with nthterm:
count=0
while count < nthterm:
    print(n1,end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

