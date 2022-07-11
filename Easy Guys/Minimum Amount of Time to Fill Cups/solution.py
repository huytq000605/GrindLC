class Solution:
    def fillCups(self, amount):
        return max(max(amount), (sum(amount)+1) // 2)
