class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        seen = set()
        result = set()
        for num in arr:
            seen = {num | prevSubarray for prevSubarray in seen} | {num}
            result |= seen
              
        return len(result)