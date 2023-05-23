a=int(input())
temp=a
b = []
c = 1
while temp!=0:
    r=temp%10
    if r not in b:
        b.append(r)
    else :
        c = 0
        break
    temp //= 10
if c :
    print("Unique Number")
else:
    print("Not Unique Number")