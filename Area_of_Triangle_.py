
a,b,c=map(int,input().split())
s=(a+b+c)/2
q=s*(s-a)*(s-b)*(s-c)
l=q**0.5
print("%.2f"%l)