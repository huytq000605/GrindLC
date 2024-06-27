class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        # a == b => a ^ b == 0 => xor(a[i..k]) == 0
        # j can be anything from i+1 to k-1
        prefix = {0: [-1, 1]}
        cur = 0
        result = 0
        for i in range(n):
            cur ^= arr[i]
            sum_idx, k = prefix.get(cur, [0, 0])
            # for each index j before i where xor(a[j..i]) == 0
            # k can be from [j+1, i-1]
            # valid sub array = i - 1 - (j + 1) + 1 = i - j - 1
            # => sum(valid sub array) = i * k - sum(j that xor(a[j..i]) == 0) - k
            result += i * k - sum_idx - k
            prefix[cur] = [sum_idx + i, k + 1]
        return result 
