class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 1:
            return trees
        trees = sorted((trees[i][0], trees[i][1]) for i in range(len(trees)))
        
        # OB is anti-clockwise to OA
        def relative_position(O, A, B):
            return (A[0] - O[0]) * (B[1] - O[1]) - (B[0] - O[0]) * (A[1] - O[1])
        
        upper = []
        for p in trees:
            while len(upper) >= 2 and relative_position(p, upper[-2], upper[-1]) > 0:
                upper.pop()
            upper.append(p)
        
        lower = []
        for p in reversed(trees):
            while len(lower) >= 2 and relative_position(p, lower[-2], lower[-1]) > 0:
                lower.pop()
            lower.append(p)

        return list(set(upper[:-1] + lower[:-1]))
            
