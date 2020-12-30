from random import randrange

def miller_rabin(n, k=16):
    """Miller-Rabin primality testing.    

    Deterministic if n < 3317044064679887385961981 (≈ 1.37 * 2**81);
    probablistic if n >= 3317044064679887385961981 (error probability < 4**-k).
    https://en.wikipedia.org/wiki/Miller-Rabin_primality_test
    
    n = Integer to be tested for primality.
    k = Number of rounds (witnesses) of testing.
    return False, if n is composite,
    return True, if n is probably prime.
    """
    
    def is_composite(a, d, n, s):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(1, s):
            x = pow(x, 2, n)
            if x == n - 1:               
                return False
            if x == 1:    
                return True
        return True # n is composite
    
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
              131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
              197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
              271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
              353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
              433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
              509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
              601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673,
              677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761,
              769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857,
              859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
              953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031)
    if n < 1033:
        return n in primes
    if any(not n % x for x in primes):
        return False
    
    # Decompose (n - 1) to write it as (2 ** s) * d
    d = n - 1
    s = 0
    while not d & 1:    # while d % 2 == 0
        d >>= 1         # d = d // 2
        s += 1
        
    # Smallest odd numbers for which Miller-Rabin primality test on bases
    # <= n-th prime does not reveal compositeness. https://oeis.org/A014233
    bases = (2047, 1373653, 25326001, 3215031751, 2152302898747,
             3474749660383, 341550071728321, 341550071728321,
             3825123056546413051, 3825123056546413051,
             3825123056546413051, 318665857834031151167461,
             3317044064679887385961981)
    for i, base in enumerate(bases, 1):
        if n < base:            
            return not any(is_composite(a, d, n, s) for a in primes[:i])
    return not any(is_composite(randrange(2, n-1), d, n, s) for a in range(k))
