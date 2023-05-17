a=int(input())
while a>9:
    r=a%10
    a=a//10
    a=a+r
print(a)    