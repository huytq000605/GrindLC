# Bit manipulation

### Position count from right to left

### Set bit at position: **mask = mask | (1 << position)**

### Unset bit at position: **mask = mask & ~(1 << position)**

### Set n bit: **mask = mask | (1 << (n * position))**

### Unset n bit: **mask = mask & ~(1 << (n * position))**

### Get most left bit:
``` typescript
for(let i = 31; i >= 0; i--) {
	if(mask & (1 << i) !== 0) {
		return i
	}
}
```


### Get most right bit:
``` typescript
for(let i = 0; i < 32; i++) {
	if(mask & (1 << i) !== 0) {
		return i
	}
}
```
