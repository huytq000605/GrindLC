class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        for log in logs:
            fn, end, time = log.split(":")
            fn = int(fn)
            time = int(time)
            if end == "start":
                end = False
            else:
                end = True
            if not end:
                if stack: 
                    result[stack[-1][1]] += time - stack[-1][0]
                stack.append([time, fn])
            else:
                result[fn] += time - stack.pop()[0] + 1
                if stack: stack[-1][0] = time + 1
        return result