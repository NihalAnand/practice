number = int(input())
remainder=0
temp = number
newnum=0
l=[]
revl=0
while(temp!=0):
    remainder = temp%8
    temp= temp//8
    l.append(remainder)
l.reverse()

print(''.join(map(str,l)))