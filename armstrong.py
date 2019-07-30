import math
number = int(input())
temp = number
size = len(str(number))
remainder=0
result=0
while(temp!=0):
    remainder= temp%10
    result = result+ math.pow(remainder, size)
    temp=temp//10
if (result == number):
    print("yes")
else:
    print("no")