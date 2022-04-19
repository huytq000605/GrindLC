class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = 0
        n = len(arr)
        for num in arr:
            if num == 1:
                ones += 1
        if ones == 0: return [0, n-1]
        if ones % 3: return [-1, -1]
        
        one = 0
        start_last_partition = 0
        for i in range(n - 1, -1, -1):
            if arr[i] == 1:
                one += 1
            if one == ones // 3:
                start_last_partition = i
                break

        result = [0, 0]
        def find(i):
            j = 0
            while arr[i] == 0:
                i += 1
            while True:
                if arr[i + j] != arr[start_last_partition + j]:
                    return -1
                j += 1
                # j == len(last_partition) <=> start_last_partition + j exceeds last partition
                if j == n - start_last_partition:
                    return i + j
                
        idx = find(0)
        if idx == -1: return [-1, -1]
        result[0] = idx - 1
        idx = find(idx)
        if idx == -1: return [-1, -1]
        result[1] = idx
        return result