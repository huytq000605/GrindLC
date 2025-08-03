import math

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = [[0,0]]
        right = [[0,0]]
        initial = 0
        startLeft = 0
        
        n = len(fruits)
        start = 0
        end = n - 1
        while start < end:
            mid = start + math.ceil((end - start + 1) / 2)
            if fruits[mid][0] >= startPos:
                end = mid - 1
            else:
                start = mid
        startLeft = start
        
        currentLeft = 0
        for i in range(startLeft, -1, -1):
            pos, num = fruits[i]
            if pos < startPos and startPos - pos <= k:
                left.append([startPos - pos, currentLeft + num])
                currentLeft += num
        
        currentRight = 0
        for i in range(startLeft, n):
            pos, num = fruits[i]
            if pos > startPos and pos - startPos <= k:
                right.append([pos - startPos, currentRight + num])
                currentRight += num
            elif pos == startPos:
                initial = num

        result = 0
            
        for l in left:
            if l[0] * 2 > k:
                break
            remain = k - l[0] * 2
            start = 0
            end = len(right) - 1
            while start < end:
                mid = start + math.ceil((end - start + 1) / 2)
                if right[mid][0] > remain:
                    end = mid - 1
                else:
                    start = mid
            result = max(result, l[1] + right[start][1])
        
        for r in right:
            if r[0] * 2 > k:
                break
            remain = k - r[0] * 2
            start = 0
            end = len(left) - 1
            while start < end:
                mid = start + math.ceil((end - start + 1) / 2)
                if left[mid][0] > remain:
                    end = mid - 1
                else:
                    start = mid
            
            result = max(result, r[1] + left[start][1])
            
        return result + initial
        