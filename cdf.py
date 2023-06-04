def cdf ( x, t ): #computa la cdf empirica para una distribucion dada, en el punto t
    xo=sorted(x)
    n=len(x)-1
    N=len(x)
    k=0
    while (xo[k]<=t) & (k<=n):
       k=k+1
    fk=float(k)
    fn=float(N)
    p=fk/fn
    return p
       
