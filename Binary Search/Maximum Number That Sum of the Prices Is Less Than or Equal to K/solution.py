class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        start = 0
        end = 10**15
        
        def valid(num):
            result = 0
            b = bin(num)[2:]
            n = len(b)
            for i in range(n):
                bit = n-i
                if bit % x != 0: continue
                left = b[:i]
                right = b[i+1:]
                # pick num to always be < left
                if left:
                    result += int(left, 2) * (2**len(right))
                # if b[i] == "1"
                # we can have a situation where num on the left == left
                if b[i] == "1":
                    
                    if not right:
                        result += 1
                    else:
                        result += int(right, 2) + 1
            return result <= k

        while start < end:
            num = start + math.ceil((end - start + 1) / 2)
            if valid(num):
                start = num
            else:
                end = num - 1
        return start
