class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        @cache
        def dfs(row, col, prev_col, prev_row):
            if col >= n:
                return dfs(row + 1, 0, 0, prev_row)
            if row >= m:
                return 0
            
            result = 0
            for mask in range(1 << n):
                turn_on_bit = 0
                valid = True
                for i in range(n):
                    if (mask >> i) & 1 == 0:
                        continue
                    if seats[row][i] == "#":
                        valid = False
                        break
                    turn_on_bit += 1
                    left, right, upper_left, upper_right = 0, 0, 0, 0
                    if i > 0:
                        left = (mask >> (i - 1)) & 1
                        upper_left = (prev_row >> (i - 1)) & 1
                    if i < n - 1:
                        right = (mask >> (i + 1)) & 1
                       upper_right = (prev_row >> (i + 1)) & 1
                    
                    if left + upper_left + right + upper_right != 0:
                        valid = False
                        break
                
                if valid:
                    result = max(result, dfs(row + 1, mask) + turn_on_bit)
            return result
        
        return dfs(0, 0) 
