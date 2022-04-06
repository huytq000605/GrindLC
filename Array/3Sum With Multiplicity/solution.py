class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        n = len(arr)
        result = 0
        
        for i in counter.keys():
            for j in counter.keys():
                k = target - i - j
                if k not in counter:
                    continue
                if i == j and j == k:
                    result += counter[i] * (counter[j] - 1) * (counter[k] - 2) // 6
                elif i == j:
                    result += (counter[i] - 1) * counter[j] * counter[k] // 2
                elif i < j < k:
                    result += counter[i] * counter[j] * counter[k]
        return result % (10**9+7)