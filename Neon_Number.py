a=int(input())
sq=a*a
su=0
while sq>0:
    r=sq%10
    su=su+r
    sq=sq//10
if su==a:
    print("Neon Number")
else:
    print("Not Neon Number")
