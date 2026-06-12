# Bit Manipulation

**Idea:** A cheat sheet of common bit tricks. Bit positions are counted from **right to left** (the least significant bit is position 0).

## Single-bit operations

- **Set bit at position:** `mask = mask | (1 << position)`
- **Unset bit at position:** `mask = mask & ~(1 << position)`

## Group / n-bit operations

- **Set the n-th group:** `mask = mask | (1 << (n * position))`
- **Unset the n-th group:** `mask = mask & ~(1 << (n * position))`

## Identity

`A | B = |A| + |B| - A & B`

(The size of the union equals the sum of sizes minus the intersection.)

## Get the most significant bit (left-most set bit)

```typescript
for(let i = 31; i >= 0; i--) {
  if(mask & (1 << i) !== 0) {
    return i
  }
}
```

## Get the least significant bit (right-most set bit)

```typescript
for(let i = 0; i < 32; i++) {
  if(mask & (1 << i) !== 0) {
    return i
  }
}
```

## Unset the right-most 1 bit

```python
mask &= (mask - 1)
```

## Enumerate all subsets of a mask

Find every mask whose set bits are all contained in the given mask.

```python
givenMask
subMask = givenMask
result = []
while subMask > 0:
  result.append(subMask)
  subMask = (subMask - 1) & givenMask # Set lowest set bit to 0 and all its right will become 1, so we & given to make them 0
return result
```
