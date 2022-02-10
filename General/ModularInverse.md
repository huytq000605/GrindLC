# Modular Inverse

(a / b) mod p = ((a mod p) * (b^(-1) mod p)) mod p

b^(-1) mod p is modular inverse of b mod p
For p=prime, b^(-1) mod p = b^(p-2) mod p
to calculate it in python, use pow(b, p-2, p)
