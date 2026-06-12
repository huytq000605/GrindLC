# Modular Inverse (Modular Division)

**Idea:** You can't divide directly under a modulus, so replace division by `b` with multiplication by `b`'s **modular inverse** — the value `b^(-1)` such that `b * b^(-1) ≡ 1 (mod p)`.

$$(a / b) \bmod p = ((a \bmod p) \cdot (b^{-1} \bmod p)) \bmod p$$

Here `b^(-1) mod p` is the modular inverse of `b` mod `p`.

## Computing the inverse (prime modulus)

When `p` is **prime**, Fermat's Little Theorem gives:

$$b^{-1} \bmod p = b^{p-2} \bmod p$$

In Python, this is a single call:

```python
pow(b, p-2, p)
```

## Fast exponentiation (when there's no built-in)

Otherwise, implement modular exponentiation (fast power) using:

- `a^b = (a*a)^(b/2)` if `b` is even
- else `a^(b-1) * a`

## Notes

- The `b^(p-2)` formula requires `p` to be prime (it follows from Fermat's Little Theorem).
