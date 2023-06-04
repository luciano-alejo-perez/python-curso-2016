def brreg(w,b,a):

    import numpy as np
    from samplerM import samplerM
    
    [n1,n2]=np.shape(w)

    x=np.array(w[:,0:n2-1])
    y=np.array(w[:,n2-1])

    d=[]  
    for k in range(0,b):
        q=[]
        s=samplerM(w)
        sx=s[:,0:n2-1]
        sy=s[:,n2-1]
        sxt= np.transpose(sx)
        q=np.dot(np.linalg.inv(np.dot(sxt,sx)),np.dot(sxt,sy))
        d.append(q)

    K=int(np.floor(b*a/2))
    d=np.array(d)
    [nd1,nd2]=np.shape(d)

    confin=[]
   
    for l in range(0,nd2):
     cl=d[:,l]   
     ds=sorted(cl)
     L=ds[K]
     U=ds[b-K]
     confin.append([L,U])

    return confin
