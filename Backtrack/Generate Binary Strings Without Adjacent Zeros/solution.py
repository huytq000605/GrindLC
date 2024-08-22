class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = ["0", "1"]
        for _ in range(n-1):
            next_result = []
            for r in result:
                if r[-1] == "0":
                    next_result.append(r + "1")
                else:
                    next_result.append(r + "1")
                    next_result.append(r + "0")
            result = next_result
        return result
