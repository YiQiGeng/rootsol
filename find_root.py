import numpy as np
from scipy.optimize import minimize



def find_zero(fn,fn_anti,min0,max0,nitermax,eps=1e-8):
  min=min0
    max=max0
    finalx=[]
    def output(fn,min,max):
            if abs(fn(min))<=eps:
                outx=min
            elif abs(fn(max))<=eps:
                outx=max
            elif abs(fn((max+min)/2))<=eps:
                outx=(max+min)/2
            else:
                outx=None
            return outx
        
    def twosol(fn,min,max,mid,nitermax):
        maxfor1=mid
        minfor2=mid
        finalx2=[]
        finalx1=[]
        for loop1 in range(nitermax):
            midfor1=(min+maxfor1)/2
            if output(fn,min,maxfor1)!=None:
                finalx1=[output(fn,min,maxfor1)]
                break
            if fn(maxfor1)*fn(midfor1)<=0:
                min=midfor1
            elif fn(min)*fn(midfor1)<=0:
                maxfor1=midfor1
            if loop1==nitermax-1 and abs(fn((min+maxfor1)/2))>eps:
                finalx1=[]
                #print("the first one is a divergence")
        for loop2 in range(nitermax):
            midfor2=(minfor2+max)/2
            if output(fn,minfor2,max)!=None:
                finalx2=[output(fn,minfor2,max)]
                break
            if fn(max)*fn(midfor2)<=0:
                minfor2=midfor2
            elif fn(minfor2)*fn(midfor2)<=0:
                max=midfor2
            if loop2==nitermax-1 and abs(fn((minfor2+max)/2))>eps:
                finalx2=[]
                #print("the second one is a divergence")
        return finalx1+finalx2
    

    # print("min",fn(min))
    # print("max",fn(max))
    if fn(min)*fn(max)<=0:
        # print("diff")
        for loop in range(nitermax):
            mid=(min+max)/2
            if output(fn,min,max)!=None:
                finalx=[output(fn,min,max)]
                #print(f"[%.4f,%.4f] find one solution! x=%.5f"%(min0,max0,finalx[0]))
                break
            if fn(max)*fn(mid)<=0:
                min=mid
            elif fn(min)*fn(mid)<=0:
                max=mid
            if loop==nitermax-1 and abs(fn((min+max)/2))>eps:
                #print(f"[%.4f,%.4f] find a divergence"%(min0,max0))
                finalx=[]
    else:
        if fn(min)>0 and fn(max)>0:
            # print("both +")
            res = minimize(fn, (min+max)/2, bounds=[(min, max)])
            if res.fun>0:
                #print(f"[%.4f,%.4f] find no solution"%(min0,max0))
                #print("Both side above zero with min=%.4f"%(res.fun[0]))
                finalx=[]
            elif abs(res.fun)<=eps:
                #print(f"[%.4f,%.4f] find one solution! x=%.5f"%(min0,max0,res.x))
                finalx=[res.x]
            else:
                mid=res.x[0]
                #print(f"[%.4f,%.4f] find two solutions!! Both side above."%(min0,max0))
                finalx=twosol(fn,min,max,mid,nitermax)
                # if len(finalx)==2:
                #     #print("x1=%.5f"%(finalx[0]),"x2=%.5f"%(finalx[1]))
                # elif len(finalx)==1:
                #     #print("x1=%.5f"%(finalx[0]),"x2 is a divergence")
                # elif len(finalx)==0:
                #     #print("Both are divergent")
        if fn(min)<0 and fn(max)<0:
            # print("both -")
            res = minimize(fn_anti, (min+max)/2, bounds=[(min, max)])
            if -1*res.fun<0:
                #print(f"[%.4f,%.4f] find no solution!!"%(min0,max0))
                #print("Both side below zero with max=%.4f"%(-1*res.fun[0]))
                finalx=[]
            elif abs(res.fun)<=eps:
                finalx=[res.x]
                #print(f"[%.4f,%.4f] find one solution! x=%.5f"%(min0,max0,res.x))
            else:
                #print(f"[%.4f,%.4f] find two solutions!! Both side below."%(min0,max0))
                mid=res.x[0]
                finalx=twosol(fn,min,max,mid,nitermax)
                # if len(finalx)==2:
                #     #print("x1=%.5f"%(finalx[0]),"x2=%.5f"%(finalx[1]))
                # elif len(finalx)==1:
                #     #print("x1=%.5f"%(finalx[0]),"x2 is a divergence")
                # elif len(finalx)==0:
                #     #print("Both are divergent")
    return finalx 
