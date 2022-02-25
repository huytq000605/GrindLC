class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1, ver2 = version1.split("."), version2.split(".")
        for i in range(max(len(ver1), len(ver2))):
            ve1, ve2 = "0", "0"
            if i < len(ver1):
                ve1 = ver1[i]
            if i < len(ver2):
                ve2 = ver2[i]
            v1, v2 = 0, 0
            for d in ve1:
                v1 = v1 * 10 + int(d)
            for d in ve2:
                v2 = v2 * 10 + int(d)
            if v1 < v2:
                return -1
            elif v1 == v2:
                continue
            else:
                return 1
        return 0
