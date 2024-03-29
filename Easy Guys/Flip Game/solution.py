class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []
        n = len(currentState)
        for i in range(1, n):
            if currentState[i] == "+" and currentState[i-1] == "+":
                result.append(currentState[:i-1] + "--" + currentState[i+1:])
        return result
