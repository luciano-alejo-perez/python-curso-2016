def samplerM( x ):
   #remuestreador de tamano n#
   from numpy import shape
   from numpy import array
   [n1,n2]=shape(x)
   s=[]
   from random import randint
   r=[randint(0,n1-1) for p in range(0,n1)]
   for k in range (0,n1):
      s.append(x[r[k],:])
   s=array(s)	
   return s

