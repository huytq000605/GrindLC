class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        palindromes = []
        left, right = int(left), int(right)
        for i in range(10):
            if left <= i * i <= right:
                palindromes.append(i)
        for i in range(1, 10000 + 1):
            s = str(i)
            num = int(s + s[::-1])
            if left <= num * num <= right:
                palindromes.append(num)
            for j in range(10):
                num = int(s + str(j) + s[::-1]) 
                if left <= num * num <= right:
                    palindromes.append(num)
        def is_palindrome(num):
            num = str(num)
            l, r = 0, len(num) - 1
            while l < r:
                if num[l] != num[r]:
                    return False
                l += 1
                r -= 1
            return True
        result = 0
    
        for num in palindromes:
            square = num * num
            if is_palindrome(square):
                result += 1
        return result