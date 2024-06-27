class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        counter = Counter(hand)
        dq = deque()
        prev_num = -1
        track = 0
        for card, freq in sorted(counter.items(), key = lambda c: c[0]):
            if (track and prev_num + 1 != card) or freq < track:
                return False
            dq.append(freq - track)
            track = freq
            if len(dq) == groupSize:
                track -= dq.popleft()
            prev_num = card
        return track == 0
            

            
