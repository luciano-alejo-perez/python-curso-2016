def bootmean( x, b ):
    mD=[]
    from numpy import mean
    from sampler import sampler
    for j in range (0,b):
        a=[]
        a=sampler(x)
        mB=[]
        mB=mean(a)
        mD.append(mB)
    return mD
