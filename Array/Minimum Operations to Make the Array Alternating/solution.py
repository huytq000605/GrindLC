class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        counter = Counter(nums[0::2])
        
        even_most_appear = (0, 0)
        even_second_most_appear = (0, 0)
        for num, count in counter.items():
            if count >= even_most_appear[0]:
                even_second_most_appear = (even_most_appear[0], even_most_appear[1])
                even_most_appear = (count, num)
            elif count > even_second_most_appear[0]:
                even_second_most_appear = (count, num)
            
        counter = Counter(nums[1::2])
        odd_most_appear = (0, 0)
        odd_second_most_appear = (0, 0)
        for num, count in counter.items():
            if count >= odd_most_appear[0]:
                odd_second_most_appear = (odd_most_appear[0], odd_most_appear[1])
                odd_most_appear = (count, num)
            elif count > odd_second_most_appear[0]:
                odd_second_most_appear = (count, num)
        
        if even_most_appear[1] == odd_most_appear[1]:
            return min(n - even_most_appear[0] - odd_second_most_appear[0], n - even_second_most_appear[0] - odd_most_appear[0])
        else:
            return n - even_most_appear[0] - odd_most_appear[0]