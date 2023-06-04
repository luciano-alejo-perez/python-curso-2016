def bootmeanI( x, b ,alpha ): #estima la media por bootstrap con su error estandar
    mD=[]
    from numpy import mean
    from sampler import sampler
    from sterr import sterr
    from numpy import floor
    esp=mean(x)
    for j in range (0,b):
        a=[]
        a=sampler(x)
        mB=[]
        mB=mean(a)
        mD.append(mB)
        m=mean(mD)
        s=sterr(mD)
    
    y=sorted(mD)
    K=int(floor(b*alpha))
    L=y[K]
    U=y[b-K]
    return [L,U]
