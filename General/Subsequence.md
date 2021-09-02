- If question asks count how many subsequence, we can sort the input

- Count subsequence (knowing start index, end index) algorithmm is using dynamic programming
  => So we know how many elements do we have by: end - start + 1
  dp is array that calculate result, with dp[i] is result for i elements we have
  dp[1] = 1
  dp[i + 1] = dp[i] * 2