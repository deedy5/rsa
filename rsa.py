from secrets import randbits
from random import randrange
from math import gcd
from miller_rabin import miller_rabin

def getprime(bits: int) -> int:
    """Generate a random bits size prime number"""
    
    #rounds of M-R test. FIPS 186-4, C.3, F.3
    if bits == 1024:
        k = 5
    elif bits == 1536:
        k = 4
    else:
        k = 10        
    while True:
        n = randbits(bits) | 1  # n += 1 if n is odd
        if miller_rabin(n, k + 1):
            return n

def rsa_keys(bits: int) -> (int, int):
    """Get public and private keys"""

    E = 65537

    if bits not in (2048, 3072):
        print('Error. Use bits == 2048 or 3072')
        return 0, 0
    
    while True:    
        p = getprime(bits//2)
        q = getprime(bits//2)   
        phi = (p - 1)*(q - 1)    
        
        # Verify that e and phi are comprime           
        if gcd(E, phi) == 1:
            n = p * q
            d = pow(E, -1, phi)
            public_key = (E, n)
            private_key = (d, n)
            return public_key, private_key    
