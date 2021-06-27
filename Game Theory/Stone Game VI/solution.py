from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        sumA = [0]* len(aliceValues)
        for idx in range(len(sumA)):
            sumA[idx] = [idx, aliceValues[idx] + bobValues[idx]]
        sumA.sort(key = lambda sumA: sumA[1], reverse = True)
        aliceTurn = True
        alicePoint = 0
        bobPoint = 0
        for s in sumA:
            if aliceTurn:
                alicePoint += aliceValues[s[0]]
                aliceTurn = False
            else:
                bobPoint += bobValues[s[0]]
                aliceTurn = True
        if alicePoint > bobPoint:
            return 1
        if alicePoint < bobPoint:
            return -1
        return 0
            
            
        