
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        def depth(num):
            return num // 100
        def pos(num):
            return num % 100 // 10 - 1
        def val(num):
            return num % 10
        dq = deque([(0, val(nums[0]))])
        result = 0
        while dq:
            k = len(dq)
            for _ in range(k):
                i, s = dq.popleft()
                is_leaf = True
                for j in range(i+1, len(nums)):
                    if depth(nums[j]) > depth(nums[i]) + 1: break
                    if depth(nums[j]) == depth(nums[i]) + 1 and \
                        (pos(nums[j]) == pos(nums[i]) * 2 or pos(nums[j]) == pos(nums[i]) * 2 + 1):
                        is_leaf = False
                        dq.append((j, s + val(nums[j])))
                if is_leaf: result += s
        return result
