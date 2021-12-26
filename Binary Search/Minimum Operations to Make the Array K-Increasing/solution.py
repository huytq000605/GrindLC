class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        result = 0
        def LIS(arr):
            n = len(arr)
            states = []
            for i in range(n):
                if len(states) == 0 or arr[i] >= states[-1]:
                    states.append(arr[i])
                else:
                    start = 0
                    end = len(states) - 1
                    while start < end:
                        mid = start + (end - start) // 2
                        if states[mid] > arr[i]:
                            end = mid
                        else:
                            start = mid + 1
                    states[start] = arr[i]
            return len(states)
        
        lists = [[] for i in range(k)]
        for i in range(n):
            lists[i % k].append(arr[i])
        
        for l in lists:
            result += len(l) - LIS(l)
        
        return result