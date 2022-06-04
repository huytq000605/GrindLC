class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        result = 0
        def max_arr(arr, k):
            stack = []
            n = len(arr)
            for i, num in enumerate(arr):
                while stack and num > stack[-1] and len(stack) - 1 + (n-i) >= k:
                    stack.pop()
                stack.append(num)
            return stack[:k]
        
        def get_first(a1, a2, i1, i2):
            if i1 >= len(a1):
                return False
            if i2 >= len(a2):
                return True
            if a1[i1] > a2[i2]:
                return True
            elif a1[i1] == a2[i2]:
                return get_first(a1, a2, i1+ 1, i2 + 1)
            else:
                return False
        
        for i in range(m+1):
            if i > k:
                break
            if n < (k - i):
                continue
            a1, a2 = max_arr(nums1, i), max_arr(nums2, k-i)
            i1, i2 = 0, 0
            num = 0
            while i1 < len(a1) or i2 < len(a2):
                num = num * 10
                if get_first(a1, a2, i1, i2):
                    num += a1[i1]
                    i1 += 1
                else:
                    num += a2[i2]
                    i2 += 1
            result = max(result, num)
        return map(int, str(result))