#Word /800
#https://codeforces.com/problemset/problem/59/A

s = input()
u = ""
l = ""
for i in s:
    if ord(i) in range(65,91):
        u+=i
    elif ord(i) in range(97,124):
        l+=i
if len(u)<=len(l):
    print(s.lower())
else:
    print(s.upper())
