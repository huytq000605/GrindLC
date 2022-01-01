class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        result = [0 for num in arr]
        n = len(arr)
        
        count = Counter()
        last_index = defaultdict(int)
        prefix = defaultdict(int)
        
        for idx, num in enumerate(arr):
            if count[num] == 0:
                last_index[num] = idx
            else:
                prefix[num] += (idx - last_index[num]) * count[num]
                result[idx] += prefix[num]
                last_index[num] = idx
            count[num] += 1
        
        count = Counter()
        last_index = defaultdict(int)
        prefix = defaultdict(int)
        
        for idx, num in enumerate(arr[::-1]):
            if count[num] == 0:
                last_index[num] = idx
            else:
                prefix[num] += (idx - last_index[num]) * count[num]
                result[n - idx - 1] += prefix[num]
                last_index[num] = idx
            count[num] += 1

        return result
