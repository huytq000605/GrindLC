class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        lookup = dict()
        for idx, num in enumerate(target):
            lookup[num] = idx
        
        new_arr = []
        for num in arr:
            if num in lookup:
                new_arr.append(lookup[num])

        states = []
        for idx in new_arr:
            if len(states) == 0 or states[-1] < idx:
                states.append(idx)
            else:
                start = 0
                end = len(states) - 1
                while start < end:
                    mid = start + (end - start) // 2
                    if states[mid] >= idx:
                        end = mid
                    else:
                        start = mid + 1
                states[start] = idx
        
        return len(target) - len(states)