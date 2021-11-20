# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
    @dp = Array.new(word1.length) { Array.new(word2.length) }
    @word1 = word1
    @word2 = word2
    def dfs(idx1, idx2)
        if idx1 >= @word1.length and idx2 >= @word2.length
            return 0
        end
        if idx1 >= @word1.length
            return @word2.length - idx2
        end
        if idx2 >= @word2.length
            return @word1.length - idx1
        end
        
        if @dp[idx1][idx2] != nil
            return @dp[idx1][idx2]
        end
        
        result = 1 << 31
        
        if @word1[idx1] == @word2[idx2]
            result = dfs(idx1 + 1, idx2 + 1)
        else
            insert = 1 + dfs(idx1, idx2 + 1)
            delete = 1 + dfs(idx1 + 1, idx2)
            replace = 1 + dfs(idx1 + 1, idx2 + 1)
            result = [insert, delete, replace].min
        end
        @dp[idx1][idx2] = result
        return result
    end
    
    return dfs(0, 0)
            
end