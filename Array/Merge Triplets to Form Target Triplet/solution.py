class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [0,0,0]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for i in range(3):
                result[i] = max(result[i], triplet[i])
        for i in range(3):
            if result[i] != target[i]:
                return False
            
        return True