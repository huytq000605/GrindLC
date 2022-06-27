class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0 for i in range(n)]
        # each key (num in arr) store a tuple with 2 values (last_idx, count, sum)
        seen = dict()
        for i in range(n):
            num = arr[i]
            if num in seen:
                last_idx, count, s = seen[num]
                seen[num] = (i, count + 1, s + (i - last_idx) * count)
                result[i] += seen[num][2]
            else:
                seen[num] = (i, 1, 0)
        
        seen = dict()
        for i in range(n-1, -1, -1):
            num = arr[i]
            if num in seen:
                last_idx, count, s = seen[num]
                seen[num] = (i, count + 1, s + (last_idx - i) * count)
                result[i] += seen[num][2]
            else:
                seen[num] = (i, 1, 0)
            
        return result
