class Solution:
    def largestOddNumber(self, num: str) -> str:
        result = ""
        odd = False
        for c in num[::-1]:
          if int(c) % 2 == 1:
            odd = True
            result += c
          elif odd:
            result += c
        return result[::-1]
