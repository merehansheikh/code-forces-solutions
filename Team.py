#Team /800
#https://codeforces.com/problemset/problem/231/A

n=int(input())
i=1
problems=0
while i<=n:
    count=0
    x=str(input())
    for c in x:
        if c!=' ':
            if int(c)&1==1:
                count=count+1
    if count>=2:
        problems+=1
    i=i+1
print (problems)
