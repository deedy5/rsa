from time import perf_counter
from random import randrange
import cProfile
from rsa import miller_rabin
from rsa import getprime
from rsa import rsa_keys


def timing(f):
    def wrap(*args):
        t1 = perf_counter()
        r = f(*args)
        print(f"\n{f.__name__} done.\nResult = {r} .\nTime = {perf_counter()-t1}")
        return r
    return wrap

@timing
def mr(n):
    return miller_rabin(n)

@timing
def get_prime(bits):
    return getprime(bits)

@timing
def rsakeys(bits):
    return rsa_keys(bits)


##"""Miller-Rabin: one n"""
##n = 2**1279-1
####n = 2**2203-1
##mr(n)
##
##"""Miller-Rabin: list"""
##t1 = perf_counter()
##primes = [x for x in range(2**1024-10000, 2**1024) if miller_rabin(x)]
##print(len(primes))
##print(perf_counter() - t1)

##rsakeys(2048)
##cProfile.run('rsakeys(3072)', sort='cumtime')
bits = 2048
"""Rsa_Keys: list"""
r = []
for _ in range(10):
    t1 = perf_counter()
    rsa_keys(bits)
    t = perf_counter() - t1
    r.append(t)
    print(_)
print(sum(r) / len(r))
