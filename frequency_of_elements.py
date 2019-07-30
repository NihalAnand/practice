'''import collections
a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
counter=collections.Counter(a)
print(counter)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
print(counter.values())
# [4, 4, 2, 1, 2]
print(counter.keys())
# [1, 2, 3, 4, 5]
print(counter.most_common(3))
# [(1, 4), (2, 4), (3, 2)]'''

def countfrequency(my_list):
    freq={}
    count=0
    for i in my_list:
        if(i in freq):
            freq[i]+=1
        else:
            freq[i]=1
    for key, value in freq.items():
        print("%d:%d"%(key,value))  #prints the keys along with their frequency
    #for k in freq.keys():
     #   count+=freq[k]
    #print(count) # counts the frequency of the values for all the keys

my_list=[1,1,1,3,4,5,6,7,8,9,3,5,7,8,5,1,3,5,6]
countfrequency(my_list)