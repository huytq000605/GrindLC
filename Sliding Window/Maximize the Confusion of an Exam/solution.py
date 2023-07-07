class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
      start = 0
      t, f = 0, 0
      result = 0
      for i, a in enumerate(answerKey):
        if a == "T": t += 1
        else: f += 1
        while min(t, f) > k:
          if answerKey[start] == "T": t -= 1
          else: f -= 1
          start += 1
        result = max(result, i - start + 1)
      return result
