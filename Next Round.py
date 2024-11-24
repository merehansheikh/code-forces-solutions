#Next Round /800
#https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
x = list(map(int, input().split()))

if k == 1:
    a = x[0]
else:
    a = x[k - 1]  

c = 0
for i in x:
    if i > 0:
        if i >= a:
            c += 1
print(c)
