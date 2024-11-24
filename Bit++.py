#Bit++ /800
#https://codeforces.com/problemset/problem/282/A

n=int(input())
x = 0
for i in range(n):
    b = input()
    if "+" in b:
        x+=1
    elif "-" in b:
        x-=1
print(x)
