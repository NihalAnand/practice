def ends(s):
    l=[]
    for i in s.split():
        if(i[-1]=="s"):
            l.append(i)
            str = ''.join(l)
    for j in l:
        print(j)


s='this was my progs'
result=ends(s)



