class ST:
    def __init__(self, start, end, val):
        self.left = self.right = None
        self.start = start
        self.end = end
        self.val = val
        self.lazy = 1
    
    def flip(self, start, end):
        if self.end < start or self.start > end:
            return
            
        if start <= self.start and self.end <= end:
            self.val = (self.end - self.start + 1) - self.val
            self.lazy *= -1
            return
         
        self.down()
        self.left.flip(start, end)
        self.right.flip(start, end)
        self.val = self.left.val + self.right.val
    
    def down(self):
        if self.lazy == -1:
            self.left.val = self.left.end - self.left.start + 1 - self.left.val
            self.right.val = self.right.end - self.right.start + 1 - self.right.val
            self.left.lazy *= self.lazy
            self.right.lazy *= self.lazy
            self.lazy = 1
        
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        def build_tree(start, end):
            node = ST(start, end, 0)
            if start == end:
                node.val = nums1[start]
                return node
            mid = start + (end - start) // 2
            left = build_tree(start, mid)
            right = build_tree(mid + 1, end)
            node.left = left
            node.right = right
            node.val += left.val + right.val
            return node
        st = build_tree(0, n-1)
        s = sum(nums2)
        result = []
        for query in queries:
            query_type = query[0]
            if query_type == 1:
                _, l, r = query
                st.flip(l, r)
            elif query_type == 2:
                _, p, _ = query
                s += st.val * p
            else:
                result.append(s)
        return result
                
        
