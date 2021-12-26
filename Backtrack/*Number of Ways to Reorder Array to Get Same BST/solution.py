class Solution:
        
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def ways(nums):
            if len(nums) <= 2:
                return 1
            left = []
            right = []
            for i in range(1, len(nums)):
                if nums[i] < nums[0]:
                    left.append(nums[i])
                else:
                    right.append(nums[i])
            leftNodes = len(left)
            rightNodes = len(right)
            totalNodes = leftNodes + rightNodes
			# combination is nCk, we put leftNodes into totalNodes
            return ways(left) * ways(right) * math.comb(totalNodes, leftNodes)
        return (ways(nums) - 1) % MOD
        