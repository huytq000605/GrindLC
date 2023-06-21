class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        # We can observe that need to turn all elements into one of element
        nums = [(nums[i], cost[i]) for i in range(n)]
        nums.sort()

        s = 0
        # If turns all elements into nums[i], what is the cost from the left
        l = [0 for _ in range(n)]
        for i in range(1, n):
            num, _ = nums[i]
            prev_num, prev_cost = nums[i-1]
            s += prev_cost
            l[i] = l[i-1] + s * (num - prev_num)
        result = l[-1]

        # Cost from the right
        s = 0
        cost = 0
        for i in range(n-2, -1, -1):
            num, _ = nums[i]
            prev_num, prev_cost = nums[i+1]
            s += prev_cost
            cost += s * (prev_num - num) 
            result = min(result, cost + l[i])
        return result


            
            
