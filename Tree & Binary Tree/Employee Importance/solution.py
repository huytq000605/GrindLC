"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        lookup = dict()
        for i, e in enumerate(employees):
            lookup[e.id] = employees[i]
                
        result = 0
        def dfs(employee):
            nonlocal result
            result += employee.importance
            for child in employee.subordinates:
                dfs(lookup[child])
        
        dfs(lookup[id])
        return result