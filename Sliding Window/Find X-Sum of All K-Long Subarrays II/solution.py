from sortedcontainers import SortedList;

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        top = SortedList()
        btm = SortedList()
        counter = defaultdict(int)
        s = 0
        result = []
        for i in range(len(nums)):
            if i >= k:
                v = (counter[nums[i-k]], nums[i-k])
                if v in top:
                    s -= v[0] * v[1]
                    top.remove(v)
                else:
                    btm.remove(v)
                counter[nums[i-k]] -= 1
                if not counter[nums[i-k]]: counter.pop(nums[i-k])
                else: btm.add((v[0] - 1, v[1]))
                while len(top) < x and btm:
                    v = btm[-1]
                    s += v[0] * v[1]
                    top.add(btm.pop())
            v = (counter[nums[i]], nums[i])
            if counter[nums[i]]:
                if v in top:
                    top.remove(v)
                    s -= v[0] * v[1]
                else:
                    btm.remove(v)
            counter[nums[i]] += 1
            top.add((v[0] + 1, v[1]))
            s += (v[0]+1)*v[1]
            while len(top) > x:
                v = top.pop(0)
                s -= v[0] * v[1]
                btm.add(v)
            if i >= k-1:
                result.append(s)
        return result

                
