class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m, n = len(bank), len(bank[0])
        prev = 0
        result = 0
        for row in range(m):
            devices = 0
            for col in range(n):
                if bank[row][col] == "1": devices += 1
            result += devices * prev
            if devices > 0:
                prev = devices
        
        return result
