class Solution:
    def minimizeStringValue(self, s: str) -> str:
        # Same set of characters will return the same result
        counter = [0 for _ in range(26)]
        offset = ord('a')
        k = 0
        result = [c for c in s]
        for c in s:
            if c != '?': counter[ord(c) - offset] += 1
            else: k += 1
        pq = [(freq, c) for c, freq in enumerate(counter)]
        heapify(pq)

        characters = []
        while k:
            freq, c = heappop(pq)
            characters.append(chr(c + offset))
            heappush(pq, (freq + 1, c))
            k -= 1
        characters.sort()
        j = 0
        for i in range(len(result)):
            if result[i] == '?': 
                result[i] = characters[j]
                j += 1
        
        return "".join(result)
        
