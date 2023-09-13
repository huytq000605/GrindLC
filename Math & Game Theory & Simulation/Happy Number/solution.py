class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        def square_digit_sum(num):
            s = 0
            while num:
                s += (num % 10) ** 2
                num //= 10
            return s
        while fast != 1:
            slow = square_digit_sum(slow)
            fast = square_digit_sum(square_digit_sum(fast))
            if slow == fast:
                break
        return fast == 1
