def sampler2( x, t ):
   "remuestreador" 
   n=len(x)
   s=[]
   from random import randint
   r=[randint(0,n-1) for p in range(0,t)]
   for k in range (0,t):
      s.append(x[r[k]])
   return s
