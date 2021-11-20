# @param {Integer} n
# @param {Integer[]} cuts
# @return {Integer}
def min_cost(n, cuts)
    @cuts = [0, *cuts.sort!, n]
    @dp = Array.new(@cuts.length) {Array.new(@cuts.length)}
    
    def dfs(s, e)
        if s + 1 == e
            return 0
        end
    
        if @dp[s][e] != nil
            return @dp[s][e]
        end
    
        result = 1 << 31 - 1
        for i in ((s + 1)...e)
            result = [result, @cuts[e] - @cuts[s] + dfs(s, i) + dfs(i, e)].min
        end
        
        @dp[s][e] = result
        return result
    end
    
    return dfs(0, @cuts.length - 1)
end
