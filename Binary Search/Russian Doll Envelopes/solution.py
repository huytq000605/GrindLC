class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda envelope: (envelope[0], -envelope[1]))
        states = []
        for (w, h) in envelopes:
            if not states or states[-1] < h:
                states.append(h)
            else:
                idx = bisect.bisect_left(states, h)
                states[idx] = h
        return len(states)