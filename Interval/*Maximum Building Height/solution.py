class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:  
        A = [[1, 0], *sorted(restrictions)]
        if A[-1][0] != n:
            A.append([n, n-1])
        m = len(A)
        result = 0
        
        for i in range(1, m):
            building_id, max_height = A[i]
            A[i][1] = min(max_height, building_id - A[i-1][0] + A[i-1][1])
        
        for i in range(m-2, -1, -1):
            building_id, max_height = A[i]
            A[i][1] = min(max_height, A[i+1][0] - building_id + A[i+1][1])
            
            max_reach = max(A[i][1], A[i+1][1])
            if A[i+1][0] - A[i][0] > abs(A[i][1] - A[i+1][1]):
                max_reach += ((A[i+1][0] - A[i][0]) - abs(A[i][1] - A[i+1][1])) // 2
            result = max(result, max_reach)

        return result