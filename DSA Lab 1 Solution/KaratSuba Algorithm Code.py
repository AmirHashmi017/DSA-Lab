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
    bd=Multiplication(b,c)
    ad_bc=Multiplication(a+b,c+d)-ac-bd
    return (ac)*10**n+(ad_bc)*10**n_2+(bd)
print(Multiplication(1234123412341234,5678567856785678))

    