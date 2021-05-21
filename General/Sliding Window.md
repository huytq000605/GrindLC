# There are 2 ways to do in sliding window problems ( different for me )

## Example : Give a binary string, find longest substring with all 1 if can flip most k zero
### #1 :  

```golang
start := 0
countZero := 0
max := 0
for end := range array {
    if array[i] == 0 {
        countZero++
    }
    for countZero > k {
        if array[start] == 0 {
            countZero--
        }
        start++
    }
    if end - start + 1 > max {
        max = end - start + 1
    }


}
return max
```

### #2:

```golang
start := 0
idxZero := make([]int, 0)
max := 0
for end := range array {
    if array[i] == 0 {
        idxZero = append(idxZero, i)
        if len(idxZero) > k {
            start = idxZero[0]
            idxZero = idxZero[1:]
        }
    }
    if end - start + 1 > max {
        max = end - start + 1
    }
}
return max
```