class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        def reverse(num):
            n = len(num)
            result = ""
            for i in range(n-1, -1, -1):
                if num[i] == "0" and result == "":
                    continue
                result += num[i]
            return result
        
        rev1 = reverse(str(num))
        rev2 = reverse(rev1)
        return rev2 == str(num)
