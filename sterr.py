def sterr ( x ):
    from numpy import array
    from numpy import mean
    from numpy import sqrt 
    m=[]
    xa=[]
    d=[]
    d2=[]
    serr=[]
    m=mean(x)
    xa=array(x)
    d=xa-m
    d2=d*d
    serr=sqrt(mean(d2))
    return serr

    
