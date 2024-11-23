#Way Too Long Words /800
#https://codeforces.com/problemset/problem/71/A

x=int(input())
for i in range (x):
    y=str(input())
    l=len(y)
    a=y[0:1]
    b=y[1:l-1]
    c=y[l-1:l]
    if l<=10:
        print (y)
    else:
        count=0
        for j in a:
            first=j
        for j in b:
            count=count+1
        for j in c:
            last=j
        print (f'{first}{count}{last}')
