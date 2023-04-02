class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []
        counter = Counter(nums)
        for num, freq in sorted(counter.items()):
            while len(result) < freq:
                result.append([])
            for i in range(freq):
                result[i].append(num)
        return result
            
            
