from secrets import randbits
from random import randrange
from math import gcd
from miller_rabin import miller_rabin

def getprime(bits: int) -> int:
    """Generate a random bits size prime number"""    
    
    while True:
        n = randbits(bits) | 1  # n += 1 if n is odd
        if n.bit_length() in (1024, 1536):
            if miller_rabin(n):
                return n

def rsa_keys(bits: int) -> (int, int):
    """Get public and private keys.

    Method: FIPS 186-4, Appendix B.3.3.
    Using these method p, q may be generated with lengths of 1024 or 1536 bits
    (512 bits shall not). FIPS186-4. Appendix B.3.1. Criteria for IFC Key Pairs
    """
    
    # exponent e shall be 16 < e < 2**256. FIPS 186-4. B.3.1
    E = 65537   

    if bits not in (2048, 3072):
        print('Error. Use bits == 2048 or 3072')
        return 0, 0

    #  all IFC keys shall follow criteria to conform to FIPS 186-4. B.3.1
    nlen = bits//2    
    lowlimit = (2**0.5) * (2**(nlen-1))
    while True:        
        p = getprime(nlen)
        if  p >= lowlimit and gcd(E, p-1) == 1:
            q = getprime(nlen)
            if abs(p - q) > 2**(nlen-100):
                if q >= lowlimit and gcd(E, q-1) == 1:                
                    # (p–1) and (q–1) shall be relatively prime to e.
                    phi = (p - 1)*(q - 1)            
                    # Verify that e and phi are comprime.       
                    if gcd(E, phi) == 1:
                        n = p * q
                        d = pow(E, -1, phi)
                        # If d ≤ 2**(bits//2), new p, q, d shall be determined.
                        if 2**nlen < d < phi:
                            public_key = (E, n)
                            private_key = (d, n)
                            return public_key, private_key 
