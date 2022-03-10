# AND_OR_GCD Notes

- These operaters are monotonic one, they can only just keep decreasing/increasing.

- It means if we want to query for any values in any given ranges, we can do that in only O(logn) times

``` python
# Take & as an example
# values[i] = every value start from anywhere and ends at i
values[0] = arr[0]
values[1] = [arr[1]] + [arr[1] & value for value in values[0]]
...
values[i + 1] = [arr[i+1]] + [arr[i+1] & value for value in values[i]] 
# len(values[i]) will always be < 20 if arr[i] <= 10^9 (Since the bit cannot change once it was 0)

```