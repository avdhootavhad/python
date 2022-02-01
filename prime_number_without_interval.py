number = int(input())
count = 0
for i in range (2,number):
    if number/i==0:
        count = 0
    else:
        count +=1
if count==1:
    print(number, "it prime number")
else:
    print(number,"it is not prime number")
