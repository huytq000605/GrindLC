class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        parts = 0
        idxs = 0
        while idxs + (3 + len(str(parts))) * parts + n > limit * parts:
            if 3 + len(str(parts)) * 2 > limit:
                return []
            parts += 1
            idxs += len(str(parts))
        
        result = []
        idx = 0
        for i in range(parts):
            suffix = f"<{i+1}/{parts}>"
            prefix = message[idx:idx + limit - len(suffix)]
            idx = idx + limit - len(suffix)
            result.append(prefix + suffix)
        return result
