from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        sl = SortedList(nums[1:1 + dist + 1])
        k -= 1
        result = sum(sl[:k]) + nums[0]
        full = True
        cur = result
        for i in range(dist + 2, len(nums)):
            # Check if the number we're gonna remove is k smallest element
            if sl.index(nums[i - dist - 1]) < k:
                cur -= nums[i-dist-1]
                full = False
            sl.remove(nums[i-dist-1])
            
            sl.add(nums[i])
            # If the number we just added is one of the k smallest element
            if sl.index(nums[i]) < k:
                # Enought elements in cur, need to remove k + 1 smallest element
                if full:
                    cur -= sl[k]
                cur += nums[i]
                full = True
            
            # Not enough elements due to removed
            if not full:
                cur += sl[k-1]
                full = True
            result = min(result, cur)
        return result
            
            
