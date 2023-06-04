def bmean( x,a,p ):
    "calcula la media y da un intervalo de confianza (nivel a) por bootstrap (p repeticiones)"
    from numpy import mean
    from numpy import floor
    from sampler import sampler
    xmean=[]

    for k in range(0,p):
        s=sampler(x)
        y=mean(s)
        x.append(y)

    n=len(x)
    ai=floor(p*n)
    bi=n-ai
    m=mean(xmean)
    a=xmean[ai]
    b=xmean[bi]

    return m
