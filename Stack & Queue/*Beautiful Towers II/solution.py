class Solution:
    def maximumSumOfHeights(self, mhs: List[int]) -> int:
        n = len(mhs)
        
        left_sum = [0 for _ in range(n)]
        stack = []
        cur = 0
        for i in range(n):
            count = 1
            while stack and stack[-1][0] >= mhs[i]:
                prev_val, c = stack.pop()
                cur -= c * prev_val
                count += c
            cur += count * mhs[i]
            stack.append((mhs[i], count))
            left_sum[i] = cur
            
        result = 0
        
        stack = []
        cur = 0
        for i in reversed(range(n)):
            count = 1
            while stack and stack[-1][0] >= mhs[i]:
                nxt_val, c = stack.pop()
                cur -= c * nxt_val
                count += c
            cur += count * mhs[i]
            stack.append((mhs[i], count))
            result = max(result, left_sum[i] + cur - mhs[i])
        return result
