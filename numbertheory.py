# number theory utilities

# greatest common divisor
gcd = lambda a,b: a if b==0 else gcd(b,a%b)	# lambda example, gcd(a,b), a>b

# least common multiple
lcm = lambda a,b: (a*b)//gcd(a,b)			# lambda example, lcm(a,b), a>b

def factors(n): 		# all factors of an integer n
    return [i for i in range(1,n+1) if n%i==0]

def isprime(n): 		# return True if n is a prime number
    if int(n)==n and n > 1:
        return all(n%i!=0 for i in range(2, int(n**.5 ) + 1))
    else:
        return False

def primes(N):  		# list of all primes up to N
    n = 2
    Pbool = [True]*(N+1)
    while n*n <= N:
        if Pbool[n]:
            for i in range(n*n, N+1, n):
                Pbool[i] = False
        n += 1
    return [p for p in range(2, N+1) if Pbool[p]]

def primefactors(Num):	# find prime factorization of Num
    pnums = primes(Num)			# get primes
    pfactors =[];				# storage for prime factors
    for k in range(len(pnums)):
        while Num%pnums[k] == 0:	# True if this prime is a factor
            pfactors.append(pnums[k])
            Num= int(Num/pnums[k]);
    return(pfactors)

def contfraction(x,N):	# N terms of continued fraction of x
    a = [0]*N			# create output list for continued fraction terms
    a[0] = int(x//1)			# grab integer portion of x
    frac = x - a[0]		# get remaining fractional part
    
    for k in range(1,N):# create other values
        if frac != 0:
            frac = 1/frac	# invert fractional part
        else:
            break			# there are no more terms
        
        a[k] = int(frac//1)	# grab integer portion left
        frac = frac%1	# new fractional part, same as frac = frac - a[k]
    return a

def findrat(x,N):
# num,den = findrat(x,N)
# find rational approximation of x
# using N terms in its continued fraction representation
    a = contfraction(x,N)
    N = len(a)-1
    n = 1
    d = a[N]
    for idx in range(N,0,-1):
        d,n = a[idx-1]*d+n, d
    return d,n

def listprod(List):	# product of list elements
    prod = 1
    for v in List:
        prod *= v
    return prod

def reducefraction(num,den):
# num,den = reducefraction(num,den)
# cancel common factors between numerator and denominator
    pfnum = primefactors(num)	# get prime factorizations of numerator
    pfden = primefactors(den)	# get prime factorizations of denominator
    k = 0						# compare numerator factors to denominator
    while True:
        if k == len(pfnum):		# done, no more values to check
            break
        value = pfnum[k]			# go through factors one by one
        if value in pfden:		# True for common factor
            pfnum.remove(value)	# remove factor from numerator
            pfden.remove(value)	# remove factor from denominator
        else:					# factor not found
            k +=1				# try next one in numerator
    return listprod(pfnum), listprod(pfden)


