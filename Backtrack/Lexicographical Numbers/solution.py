class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num = 1
        result = []
        for _ in range(n):
            result.append(num)
            if num * 10 <= n:
                num *= 10
            elif num % 10 != 9 and num + 1 <= n:
                num += 1
            else:
                while num % 10 == 9 or num == n: num = num // 10
                num += 1
        return result
            
