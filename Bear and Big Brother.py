#Bear and Big Brother /800
#https://codeforces.com/problemset/problem/791/A

l,b = map(int, input().split())
i = 0
while l<=b:
    l = l*3
    b = b*2
    i = i+1
print (i)
