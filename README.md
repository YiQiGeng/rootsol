# rootsol
Dichotomy root finding code. It can find at most two solutions at one time. Therefore, the solution finding section should be smaller enough.



### This methon requires max-min is smaller enough, because it can't solve no more than two solutions at one time       

### Notice that the return is a list, so one should use + to add them together when using       


### Parameter instructions
  fn is your function, and it -fn also should be given as fn_anti.
  min0 is the left side of your section, and max0 is right one.
  nitermax is the maximum number of iteration, No matter if sloution is found or not .
  eps is the accuracy of "f(x)=0".
