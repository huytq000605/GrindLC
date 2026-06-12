# Combinations, Permutations, and Factorials

**Idea:** Quick reference for the core counting formulas. To evaluate these under a modulus, you usually need the modular inverse — see `ModularInverse.md`.

## Combination (nCk)

Number of ways to choose `k` items from `n` where order does **not** matter:

$$nCk = \frac{n!}{k! \, (n-k)!}$$

Useful identities:

- $\sum_{k=0}^{n} nCk = 2^n$
- $\sum_{\substack{k=1 \\ k \text{ odd}}}^{n} nCk = 2^{n-1}$ (sum over odd `k`)
- $nCk = (n-1)Ck + (n-1)C(k-1)$ (Pascal's rule)

## Permutation (nPk)

Number of ways to arrange `k` items out of `n` where order **does** matter:

$$nPk = \frac{n!}{(n-k)!}$$

## Factorial (n!)

$$n! = 1 \cdot 2 \cdot 3 \cdots n$$
