class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mn = min(nums)
        result = 0
        # increase the min num up to max
        # old max now is min value, increase up to new max
        # do that until all the element is the same
        # we could see each time is diff of num vs the min num

        # OR

        # Increase n-1 element except the max => Decrease the max by 1
        # The problem become decrease each number to the minNumber

        for num in nums:
            result += num - mn
        return result


