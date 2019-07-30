

def rearrangingarray(arr,N):
    left=arr[0::1]
    right=arr[0::2]

    if(sorted(left)==sorted(right)):
        return('YES')
    elif(sorted(left)==sorted(right,reverse=True)):
        return('YES')
    elif(sorted(left, reverse=True)== sorted(right, reverse=True)):
        return('YES')
    elif(sorted(left,reverse=True)== sorted(right)):
        return('YES')
    else:
        return('NO')

t=int(input())
result=0
for i in range(t):
    arr_size=int(input())
    arr=list(map(int,input().split()))
result = rearrangingarray(arr, arr_size)
print(result)
print(arr)


