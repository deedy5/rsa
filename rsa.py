from secrets import randbits
from miller_rabin import miller_rabin

def generate_prime(bits):
    while True:
        n = randbits(bits)
        if n & 1 and miller_rabin(n):
            return n     
