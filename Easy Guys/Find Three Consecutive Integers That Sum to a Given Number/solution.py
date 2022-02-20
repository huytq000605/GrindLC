class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        num -= 3
        if num % 3 != 0:
            return []
        first = num // 3
        return [first, first + 1, first + 2]