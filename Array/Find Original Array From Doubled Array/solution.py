class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        if counter[0] % 2 == 1:
            return []
        
        result = [0] * (counter[0] // 2)
        for num in sorted(counter.keys()):
            if num == 0:
                continue
            if counter[num * 2] < counter[num]:
                return []
            counter[num * 2] -= counter[num]
            result += [num] * counter[num]
        return result
