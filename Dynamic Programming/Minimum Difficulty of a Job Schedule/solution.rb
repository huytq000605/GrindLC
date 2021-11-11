# @param {Integer[]} job_difficulty
# @param {Integer} d
# @return {Integer}
def min_difficulty(job_difficulty, d)
    @jobs = job_difficulty
    @MAX_INT = 1 << 31 - 1
    @dp = Array.new(job_difficulty.length) { Array.new(d + 1) }
    
    def dfs(idx, day)
        if (idx >= @jobs.length && day > 0) || (day < 0) || (@jobs.length - idx < day)
            return @MAX_INT
        end
        if idx >= @jobs.length && day == 0
            return 0
        end
        if @dp[idx][day] != nil 
            return @dp[idx][day]
        end
        result = @MAX_INT
        maxDifficult = 0
        for i in (idx...@jobs.length)
            maxDifficult = [maxDifficult, @jobs[i]].max
            result = [result, maxDifficult + dfs(i + 1, day - 1)].min
        end
        @dp[idx][day] = result
        result
    end
    
    result = dfs(0, d)
    if result >= @MAX_INT
        return -1
    end
    
    return result
end