# My library
# most of these are simply placeholders for syntax that I want to remember

def horner(p,x): # evaluate polynomial p at value x
    val=0
    for i in p:
        val = val*x+i
    return val

def iseven(n): # return True if x is even
    return n%2 == 0

def linspace(a,b,n): # create a linearly spaced list
    if n < 2:
        return b
    diff = (float(b) - a)/(n - 1)
    return [diff*i + a for i in range(n)]

def trapz(y,dx): # trapezoidal integration using data points and spacing
    return sum([(y[i]+y[i+1])*dx/2 for i in range(0,len(y)-1)])

def cumsum(y): # cummulative sum of a list
    clist = [sum(y[0:i]) for i in range(0,len(y)+1)]
    return clist[1:] 

def cumtrapz(y,dx): # cummulative trapezoidal integration
    z = [(y[i]+y[i+1])*dx/2 for i in range(0,len(y)-1)]
    return cumsum(z) 

def gradient(y,dx): # gradient using data points and spacing
    z = [(y[i+1]-y[i-1])/(2*dx) for i in range(1,len(y)-1)] # central differences
    z.insert(0,(y[1]-y[0])/dx) # forward difference at start
    z.append((y[-1]-y[-2])/dx) # backward difference at end
    return z 

def macheps(x = 1): # machine eps, x+eps>x
    return abs(x)*2.220446049250313e-16 

def getdigits(num): # return digits of an integer
    s = str(abs(int(num)))
    return [int(s[i]) for i in range(0,len(s))]

