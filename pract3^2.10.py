k=int(input())
c=int(input())
if k<5 and c>4:
    x=k+c**2
elif k>c and k>3:
    x=c**2+2
else:
    x=c-1
print(x)