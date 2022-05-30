class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = Counter()
        n = len(messages)
        for i in range(n):
            words = len(messages[i].split(" "))
            counter[senders[i]] += words
        result = 0
        result_sender = ""
        for sender, words in counter.items():
            if words > result:
                result = words
                result_sender = sender
            elif words == result:
                if result_sender < sender:
                    result_sender = sender
        return result_sender