from find_root import *

### It is a simple test that when you know where the root may lie.
### However, when facing various problem, you should give a loop of finding root operation, to make sure there is no root being omitted.

def func(x):
    #return x**2-x-2
    #return 2*x+1
    return np.cos(x)/np.sin(x)
def func_anti(x):
    return -1*func(x)

min=-np.pi/4
max=np.pi/1.5
a=find_zero(func,func_anti,min,max,100)

if len(a)==1:
    print("x=",a[0])
    print("f(x)=",func(a[0]))
elif len(a)==2:
    print("x1=",a[0])
    print("x2=",a[1])
    print("f(x1)=",func(a[0]))
    print("f(x2)=",func(a[1]))
elif len(a)==0:
    print("No solution!!")

