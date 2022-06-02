# Build consecutive values from 0

## Example:
- #330
- #1798

## Intuition
- If we have coins [1], we can form the sequence 0, 1. For extending sequence we need coin <= 2.
- If we have coing [1, 2], we can form 0, 1, 2, 3. For extending sequence we need coin <= 4.
- If we have coing [1, 2, 3], we can form 0, 1, 2, 3, 4, 5, 6. For extending sequence we need coin <= 7.
- In each of the above case, if the next coin we get is greater than the maximum sequence currently formed, we cannot extend the sequence in any case whatsoever.

## Conclusion
- So we can always sort the input and try to go from 0
- If the arr[i] is <= cur_sum + 1, then we can add it, cur_sum will be cur_sum = cur_sum + arr[i]
- If arr[i] > cur_sum + 1, then we cannot make it


