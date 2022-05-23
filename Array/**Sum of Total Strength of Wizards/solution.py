class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        next_smaller = [n for i in range(n)]
        prev_smaller = [-1 for i in range(n)] # or equal, to avoid duplication
        prefix = [0 for i in range(n)]
        prefix_prefix = [0 for i in range(n)]
        MOD = 10**9 + 7
        
        stack = []
        for i in range(n):
            while stack and strength[i] < strength[stack[-1]]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1, -1):
            while stack and strength[i] <= strength[stack[-1]]:
                prev_smaller[stack.pop()] = i
            stack.append(i)
            
        for i in range(n):
            if i > 0:
                prefix[i] = prefix[i-1]
                prefix_prefix[i] = prefix_prefix[i-1]
                
            prefix[i] += strength[i]
            prefix[i] %= MOD
            
            prefix_prefix[i] += prefix[i]
            prefix_prefix[i] %= MOD


        result = 0
        for i in range(n):
            l, r = prev_smaller[i] + 1, next_smaller[i] - 1
            
            # start at l: 
            ## end at i:        prefix[i] - prefix[l-1]
            ## end at i + 1:    prefix[i+1] - prefix[l-1]
            ## ...
            ## end at r:        prefix[r] - prefix[l-1]
            # ...
            # start at i:
            ## end at i:        prefix[i] - prefix[i-1]
            ## ...
            ## end at r:        prefix[r] - prefix[i-1]
            
            # Positive part: (prefix_prefix[r] - prefix_prefix[i-1]) * (i - l + 1)
            # Negative part: (prefix_prefix[i-1] - prefix_prefix[l-2]) * (r-i+1)
            if i > 0:
                positive_part = (prefix_prefix[r] - prefix_prefix[i-1]) * (i-l+1)
            else:
                positive_part = prefix_prefix[r] * (i-l+1)
            
            if i > 0:
                if l > 1:
                    negative_part = (prefix_prefix[i-1] - prefix_prefix[l-2]) * (r-i+1)
                else:
                    negative_part = prefix_prefix[i-1] * (r-i+1)
            else:
                negative_part = 0
            
            result += (positive_part - negative_part) * strength[i]
            result %= MOD
            result += MOD
            result %= MOD
        return result

        