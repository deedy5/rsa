[![alt text](https://img.shields.io/badge/python-3.8-red)](https://python.org)
---
# RSA
RSA implementation in Python 

Made in accordance with: [Digital Signature Standard (DSS) (FIPS 186-4)](https://csrc.nist.gov/publications/detail/fips/186/4/final)

1. Public and Private keys generation. FIPS 186-4: 5.1, APPENDIXes B.3, F.1, F.3.
    - Length of the modulus (i.e., nlen): 2048 and 3072 bits.
    - Primes generation: Miller-Rabin algorithm. FIPS 186-4 APPENDIXes B.3.3, C.3.1.
