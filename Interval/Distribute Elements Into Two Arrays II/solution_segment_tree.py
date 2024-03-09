from sortedcontainers import SortedList

class ST:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(4*n)]
    
    def query(self, start, end, idx = 0, left = 0, right = -1):
        if right == -1: right = self.n - 1
        if end < left or start > right:
            return 0
        if left >= start and right <= end:
            return self.tree[idx]
        mid = left + (right - left) // 2
        l = self.query(start, end, idx * 2 + 1, left, mid)
        r = self.query(start, end, idx * 2 + 2, mid + 1, right)
        return l + r
    
    def add_one(self, val, idx = 0, left = 0, right = -1):
        if right == -1: right = self.n - 1
        if val < left or val > right:
            return 0
        if val == left == right:
            self.tree[idx] += 1
            return
        mid = left + (right - left) // 2
        self.add_one(val, idx * 2 + 1, left, mid)
        self.add_one(val, idx * 2 + 2, mid + 1, right)
        self.tree[idx] += 1


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
            arr1, arr2 = [nums[0]], [nums[1]]
            compressed = dict()
            max_c_num = 0
            for num in sorted(nums):
                if num not in compressed:
                    compressed[num] = max_c_num
                    max_c_num += 1
            n = len(compressed)
            st1, st2 = ST(n), ST(n)
            st1.add_one(compressed[nums[0]])
            st2.add_one(compressed[nums[1]])

            for num in nums[2:]:
                c_num = compressed[num]
                c1, c2 = st1.query(c_num + 1, max_c_num-1), st2.query(c_num+1, max_c_num-1)
                if c1 > c2:
                    st1.add_one(c_num)
                    arr1.append(num)
                elif c1 < c2:
                    st2.add_one(c_num)
                    arr2.append(num)
                else:
                    if len(arr1) <= len(arr2):
                        st1.add_one(c_num)
                        arr1.append(num)
                    else:
                        st2.add_one(c_num)
                        arr2.append(num)
            return arr1 + arr2
            
