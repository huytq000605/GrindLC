# Bit manipulation

### Position count from right to left

### Set bit at position: **mask = mask | (1 << position)**

### Unset bit at position: **mask = mask & ~(1 << position)**

### Set n bit: **mask = mask | (1 << (n * position))**

### Unset n bit: **mask = mask & ~(1 << (n * position))**

### Get most left bit (Most Significant Bit):
``` typescript
for(let i = 31; i >= 0; i--) {
	if(mask & (1 << i) !== 0) {
		return i
	}
}
```


### Get most right bit (Least Significant Bit):
``` typescript
for(let i = 0; i < 32; i++) {
	if(mask & (1 << i) !== 0) {
		return i
	}
}
```

### Unset the right most 1 bit:
``` python
	mask &= (mask - 1)

```

### Get all subset of mask (finding all mask that have all set bit in given mask):
``` python
	givenMask
	subMask = givenMask
	result = []
	while subMask > 0:
		result.append(subMask)
		subMask = (subMask - 1) & givenMask # Set lowest set bit to 0 and all its right will become 1, so we & given to make them 0
	return result
```