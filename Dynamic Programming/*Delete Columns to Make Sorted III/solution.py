class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        dp = [1] * m
		# LIS
        for i in range (m):
            for j in range(0, i):
				# Go to each string
                for k in range(n + 1):
					# k == n => every string match
                    if k == n:
                        dp[i] = max(dp[i], dp[j] + 1)
                    else:
                        st = strs[k]
                        if st[j] > st[i]:
                            break
        return m - max(dp)
                        