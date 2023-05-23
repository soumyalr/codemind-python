n=int(input())
if n<0:
    n=-n
    b=str(n)
    print(-1*int(b[::-1]))
else:
    c=str(n)
    print(int(c[::-1]))
    
    
    