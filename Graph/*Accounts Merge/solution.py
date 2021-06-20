from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        for account in accounts:
            for i, email in enumerate(account):
                if i == 0: continue
                if graph.get(account[i]) == None: graph[account[i]] = set()
                if i == len(account) - 1: continue
                if graph.get(account[i+1]) == None: graph[account[i+1]] = set()
                graph.get(account[i]).add(account[i+1])
                graph.get(account[i+1]).add(account[i])
        
        def dfs(emails, email, seen):
            if seen.get(email) != None:
                return
            seen[email] = True
            emails.append(email)
            for connectedEmail in graph.get(email):
                dfs(emails, connectedEmail, seen)
            
            
            
        result = []
        seen = {}
            
        for account in accounts:
            username = account[0]
            emails = []
            for i, email in enumerate(account):
                if i == 0: continue
                dfs(emails, email, seen)
            if len(emails) == 0:
                continue
            emails.sort()
            bePushedAccount = [username] + emails
            result.append(bePushedAccount)
        
        return result