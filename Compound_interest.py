p,r,t=map(int,input().split())
ci=p*(pow((1+r/100),t))
print(format(ci,".2f"))