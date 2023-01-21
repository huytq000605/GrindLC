class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)
        ip = []
        def dfs(i):
            if i >= n:
                if len(ip) == 4:
                    result.append(".".join(ip))
                return
            if ip: nxt = int(ip[-1]) * 10 + int(s[i])
            else: nxt = 256
            if nxt < 256 and ip[-1] != "0":
                ip[-1] = str(nxt)
                dfs(i+1)
                ip[-1] = str(nxt // 10)
            if len(ip) < 4:
                ip.append(s[i])
                dfs(i+1)
                ip.pop()
        dfs(0)
        return result
                
