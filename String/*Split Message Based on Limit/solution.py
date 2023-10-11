class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        parts = 0
        prefix = 0
        # <prefix/suffix>
        # 3 is space for </>
        while prefix + (3 + len(str(parts))) * parts + len(message) > parts * limit:
            # if the space of part annotation is gte to limit than no space for message
            if len(str(parts)) * 2 + 3 >= limit:
                return []
            parts += 1
            # each time parts increase by 1, prefix inscreae by len(str(parts))
            prefix += len(str(parts))
        
        result = []
        idx = 0
        for part in range(parts):
            annotation = f"<{part+1}/{parts}>"
            msg = message[idx:idx+limit-len(annotation)]
            idx += len(msg)
            result.append(msg+annotation)
        return result
