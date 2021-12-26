from collections import Counter

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        dontSpeak = set()
        
        for u, v in friendships:
            if languages[u-1] & languages[v-1]: continue # Intersect set
            dontSpeak.add(u)
            dontSpeak.add(v)

        maxAlreadyKnow = 0
        alreadyKnow = Counter()
        for person in dontSpeak:
            for language in languages[person - 1]:
                alreadyKnow[language] += 1
                maxAlreadyKnow = max(maxAlreadyKnow, alreadyKnow[language])
        
        return len(dontSpeak) - maxAlreadyKnow