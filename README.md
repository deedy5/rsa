[![alt text](https://img.shields.io/badge/python-3.8-red)](https://python.org)

# RSA
RSA key generations in Python

`Time of rsa keys generation:
2048 bits ≈ 0.7 s.
3072 bits ≈ 2,1 s.`

### Made in accordance with: [FIPS 186-4](https://csrc.nist.gov/publications/detail/fips/186/4/final) 

The RSA Digital Signature Algorithm:

1. Public and Private keys generation. FIPS 186-4: 5.1, APPENDIXes B.3, F.1, F.3.
    - Length of the modulus: 2048 and 3072 bits.
    - Primes generation: Miller-Rabin algorithm. FIPS 186-4 APPENDIXes B.3.3, C.3.1.
    - Number of rounds (witnesses) of Miller-Rabin testing k = 40 (error probability 2**-80). FIPS 186-4, F.1.

### Usage:

Generate RSA keys, default bits = 2048:
```
python3 rsa.py
```
