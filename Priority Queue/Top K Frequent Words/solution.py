class HeapNode:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pq = []
        counter = Counter(words)
        for word, freq in counter.items():
            heappush(pq, HeapNode(word, freq))
            if len(pq) > k:
                heappop(pq)
        result = []
        while pq: result.append(heappop(pq).word)
        return result[::-1]
            
