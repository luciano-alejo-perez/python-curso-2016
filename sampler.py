def sampler( x ):
   #remuestreador de tamano n#
   n=len(x)
   s=[]
   from random import randint
   r=[randint(0,n-1) for p in range(0,n)]
   for k in range (0,n):
      s.append(x[r[k]])
   return s
