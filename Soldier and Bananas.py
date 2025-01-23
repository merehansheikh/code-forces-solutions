#Soldier and Bananas /800
#https://codeforces.com/problemset/problem/546/A

k,n,w = map(int, input().split())

t = 0
for i in range(1,w+1):
    t+=i*k

if t>n:
    print(t-n)
else:
    print(0)
