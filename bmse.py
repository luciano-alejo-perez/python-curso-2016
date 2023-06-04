def bootmean( x, b ): #estima la media por bootstrap con su error estandar
    mD=[]
    from numpy import mean
    from sampler import sampler
    from sterr import sterr
    for j in range (0,b):
        a=[]
        a=sampler(x)
        mB=[]
        mB=mean(a)
        mD.append(mB)
        m=mean(mD)
        s=sterr(mD)
    return s
