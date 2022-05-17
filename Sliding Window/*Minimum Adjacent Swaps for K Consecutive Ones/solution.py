class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        elif k == 2:
            result = math.inf
            prev = -1       
            for i in range(len(nums)):
                if nums[i] == 1:
                    if prev != -1:
                        result = min(result, i - prev - 1)
                    prev = i
            return result
        else: # If k >= 3
            i = 0
            idxs = deque()
            result = math.inf
            swaps = 0

            # Build first k consecutive ones
            while len(idxs) < k:
                if nums[i] == 1:
                    idxs.append(i)
                i += 1

            # Cost = everything around median
            median = k // 2
            # number of 1s on the left and right of median
            left_median = 0
            right_median = 0

            # Try to move all left and right to median
            for j in range(median-1, -1, -1):
                swaps += idxs[median] - idxs[j]
                left_median += 1
            
            for j in range(median + 1, k):
                swaps += idxs[j] - idxs[median]
                right_median += 1
            
            # Move k - 1 from median to make a length k sliding window
            plus = (left_median + 1) * left_median // 2 + (right_median + 1) * right_median // 2

            result = swaps - plus
            while i < len(nums):
                # Each time meet 1, delete first 1, append an 1, median also move
                if nums[i] == 1:
                    # Every 1 on the left of median and median itself + distance to new median 
                    # (except the first 1 which will be remove)
                    swaps += (left_median) * (idxs[median + 1] - idxs[median])
                    # Every 1 on the right median - distance to old median
                    swaps -= (right_median) * (idxs[median + 1] - idxs[median])
                    # Remove first 1
                    swaps -= idxs[median] - idxs[0]
                    idxs.append(i)
                    idxs.popleft()
                    # Append new 1
                    swaps += idxs[-1] - idxs[median]
                    result = min(result, swaps - plus)
                i += 1
            return result
