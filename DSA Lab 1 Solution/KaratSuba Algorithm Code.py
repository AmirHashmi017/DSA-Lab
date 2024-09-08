def Multiplication(x,y):
    if(x<10 or y<10):
        return x*y
    n=max(len(str(x)),len(str(y)))
    n_2=n//2
    a=x//10**(n_2)
    b=x%10**(n_2)
    c=y//10**(n_2)
    d=y%10**(n_2)
    ac=Multiplication(a,c)
    ad=Multiplication(a,d)
    bc=Multiplication(b,c)
    bd=Multiplication(b,c)
    return (a*c)*10**n+(a*d+b*c)*10**n_2+(b*d)
print(Multiplication(1234123412341234,5678567856785678))

    