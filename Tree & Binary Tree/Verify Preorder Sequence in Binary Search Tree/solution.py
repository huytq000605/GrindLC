class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        st = []
        mn = -math.inf
        for p in preorder:
            if p < mn: return False
            while st and p > st[-1]:
                mn = st.pop()
            st.append(p)
        return True
