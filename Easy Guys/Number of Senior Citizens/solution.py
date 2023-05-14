class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                result += 1
        return result
