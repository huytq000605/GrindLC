class Solution:
    def numberOfSteps(self, num: int) -> int:
      if num == 0:
        return 0
      result = 0
      while num > 0:
        # subtract then divide
        if num & 1:
          result += 2
        else:
          result += 1
        num >>= 1
      # Edge case: num == 1 then just need to subtract
      return result - 1