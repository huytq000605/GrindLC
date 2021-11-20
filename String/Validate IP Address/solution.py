class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ip = 0
        for l in queryIP:
            if l == ".":
                ip = 4
                break
            elif l == ":":
                ip = 6
                break
        if ip == 0:
            return "Neither"
        elif ip == 4:
            parts = queryIP.split(".")
            if len(parts) != 4: return "Neither"
            for part in parts:
                if not part.isnumeric():
                    return "Neither"
                if part[0] == "0" and len(part) > 1:
                    return "Neither"
                if int(part) > 255:
                    return "Neither"
            return "IPv4"
        else:
            parts = queryIP.split(":")
            if len(parts) != 8: return "Neither"
            for part in parts:
                if len(part) < 1 or len(part) > 4:
                    return "Neither"
                for l in part:
                    if not ((l >= 'a' and l <= 'f') or (l >= 'A' and l <= 'F') or l.isdigit()):
                        return "Neither"
            return "IPv6"
    