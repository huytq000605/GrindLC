class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        cur = ""
        for l in s:
            cur += l
            if len(cur) == k:
                result.append(cur)
                cur = ""
        if len(cur) > 0:
            cur += fill * (k - len(cur))
            result.append(cur)
        return result