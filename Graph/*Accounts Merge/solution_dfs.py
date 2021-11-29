class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for account in accounts:
            emails = account[1:]
            n = len(emails)
            if n == 1:
                graph[emails[0]] = set()
            else:
                for i in range(n - 1):
                    graph[emails[i]].add(emails[i+1])
                    graph[emails[i+1]].add(emails[i])
        seen = set()
        def dfs(email, emails):
            if email in seen:
                return
            emails.append(email)
            seen.add(email)
            for nextEmail in graph[email]:
                dfs(nextEmail, emails)
        result = []        
        for account in accounts:
            name = account[0]
            emails = []
            dfs(account[1], emails)
            if len(emails) == 0:
                continue
            emails.sort()
            result.append([name, *emails])
        
        return result