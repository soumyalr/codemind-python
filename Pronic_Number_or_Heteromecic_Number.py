n=int(input())
d=0
for i in range(1,n):
    if n%i==0:
        if i*(i+1)==n:
            d+=1
            break
if d==1:
    print("YES")
else:
    print("NO")