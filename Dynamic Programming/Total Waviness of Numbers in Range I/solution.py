class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # waviness(num) = total waviness from 1 to num
        def waviness(num):
            snum = str(num)
            @cache
            def dfs(i, prev, prev_prev, tight, started, waviness):
                if i == len(snum):
                    return waviness
                mx = int(snum[i]) if tight else 9
                nprev_prev = prev
                result = 0
                for d in range(mx+1):
                    if started >= 2 and ((prev > prev_prev and prev > d) or (prev < prev_prev and prev < d)):
                        result += dfs(i+1, d, prev, tight and int(snum[i]) == d, started, waviness + 1)
                    else:
                        result += dfs(i+1, d, prev, tight and int(snum[i]) == d, min(2, started + (1 if (d > 0 or started) else 0)), waviness)
                return result
            return dfs(0, 0, 0, True, False, 0)
        return waviness(num2) - waviness(num1-1)

