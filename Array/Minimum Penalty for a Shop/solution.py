class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        # penalties[i] = penalty if close at i
        penalties = [0 for i in range(n+1)]
        penalty = 0
        for i, c in enumerate(customers):
            if c == "N":
                penalty += 1
            penalties[i+1] = penalty
        
        penalty = 0
        for i in range(n-1, -1, -1):
            if customers[i] == "Y":
                penalty += 1
            penalties[i] += penalty
        
        mn = min(penalties)
        return penalties.index(mn)
        
        
