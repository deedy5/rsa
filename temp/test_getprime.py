from secrets import SystemRandom
from math import gcd, lcm
from decimal import Decimal
import cProfile
from time import perf_counter

from miller_rabin import miller_rabin

E = 65537 # exponent e shall be 2**16 < e < 2**256. FIPS 186-4. B.3.1

def getprime(bits: int) -> int:
    """Generate a random bits size prime number"""
    
    secure_randrange = SystemRandom().randrange    
    #  prime shall be (lowlimit < p < 2**bits-1). FIPS 186-4. B.3.1
    lowlimit = int(Decimal(2**0.5) * Decimal(2**(bits-1)))
    highlimit = 2**bits-1    
    while True:
        p = secure_randrange(lowlimit, highlimit) | 1  # n += 1 if n is odd
        # (p–1) shall be relatively prime to e. FIPS 186-4. B.3.1
        if gcd(E, p-1) == 1:            
            if miller_rabin(p):
                return p


##getprime(1536)
##t1 = perf_counter()
##r = [getprime(1024) for _ in range(10)]
##print((perf_counter() - t1) / len(r))
cProfile.run('getprime(1024)', sort='cumtime')

