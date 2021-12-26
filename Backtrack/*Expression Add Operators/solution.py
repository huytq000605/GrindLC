class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        def dfs(idx, path, value, prev):
            if idx >= len(num):
                if value == target:
                    result.append(path)
                return
            for i in range(idx, len(num)):
                if num[idx] == "0" and i != idx:
                    break
                string = num[idx: i + 1]
                parse = int(string)
                if idx == 0:
                    dfs(i + 1, string, parse, parse)
                else:
                    dfs(i + 1, path + "+" + string, value + parse, parse)
                    dfs(i + 1, path + "-" + string, value - parse, -parse)
                    dfs(i + 1, path + "*" + string, value - prev + prev * parse, prev * parse)
        dfs(0, "", 0, 0)
        return result