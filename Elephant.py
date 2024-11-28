#Elephant /800
#https://codeforces.com/problemset/problem/617/A

x = int(input())
s = x//5
if x%5!=0:
    print(s+1)
else:
    print(s)
