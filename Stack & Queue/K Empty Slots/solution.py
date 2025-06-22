class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        days = [0 for _ in range(n)]
        for i in range(n):
            days[bulbs[i]-1] = i+1
        st = []
        result = n+1
        for b in range(n):
            while st and days[b] <= days[st[-1]]:
                if b - st[-1] == k+1:
                    result = min(result, days[st[-1]])
                st.pop()
            if st and b - st[-1] == k+1:
                result = min(result, days[b]) 
            st.append(b)
        return result if result <= n else -1
