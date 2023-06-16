# Modular Inverse

(a / b) mod p = ((a mod p) * (b^(-1) mod p)) mod p

b^(-1) mod p is modular inverse of b mod p
For p=prime, b^(-1) mod p = b^(p-2) mod p

To calculate it in python, use pow(b, p-2, p)
Otherwise, need to implement pow with module by:
a^b = (a*a)^(b/2) if b is even
else a^(b-1)*a
