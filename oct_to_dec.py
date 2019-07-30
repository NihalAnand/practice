import math
number= int(input())
temp=number
remainder=0
result=0
i=0
while(temp!=0):
    remainder= temp%10
    result= result + remainder * math.pow(8, i)
    temp//=10
    i+=1

print(result)