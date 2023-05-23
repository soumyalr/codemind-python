a=int(input())
su=0
mul=1
while a!=0:
    r=a%10
    su=su+r
    mul=mul*r
    a=a//10   
if su==mul:
    print("Spy Number")
else:
    print("Not Spy Number")
    