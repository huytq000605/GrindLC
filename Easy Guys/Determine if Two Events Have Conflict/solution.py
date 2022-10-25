class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        e1_from = int(event1[0][:2]) * 60 + int(event1[0][3:])
        e1_to = int(event1[1][:2]) * 60 + int(event1[1][3:])
        e2_from = int(event2[0][:2]) * 60 + int(event2[0][3:])
        e2_to = int(event2[1][:2]) * 60 + int(event2[1][3:])
        if min(e1_to, e2_to) < max(e1_from, e2_from):
            return False
        return True
