class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = Counter()
        for num in arr:
            freq[num % k] += 1
        for val in freq.keys():
            if val == 0 or k - val == val:
                if freq[val] % 2 != 0:
                    return False
            else:
                if freq[k - val] != freq[val]:
                    return False
        return True
