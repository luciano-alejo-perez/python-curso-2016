def dble ( x ):
    from numpy import mean
    from bserr import meansterr
    m=mean(x)
    se=meansterr(x)
    r=[m,se]
    return r
