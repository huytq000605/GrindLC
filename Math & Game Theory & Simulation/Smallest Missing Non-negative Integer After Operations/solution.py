class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = Counter()
        for num in nums:
            counter[num % value] += 1
        for i in range(10**5):
            if counter[i % value] == 0:
                return i
            counter[i % value] -= 1
        return 10**5
            
