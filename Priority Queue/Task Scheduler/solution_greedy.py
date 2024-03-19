class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        most_freq = max(counter.values())
        count_most_freq = sum(1 if v == most_freq else 0 for v in counter.values())
        # Divide the tasks into `most_freq` groups
        # Each group will start with character has freq = most_freq
        # That means first char of each group needs to have at least n spaces between
        # first `most_freq - 1` groups, each will take at least (n+1) spaces
        # Last group, only characters with freq = most_freq are left
        # So last group will take (count_most_freq)
        
        # The algorithm above focuses on the max frequency task, 
        # and its result is as soon as that task can be completed. 
        # However, if you have more total work than 
        # gaps that the max frequency element needs
        # you are guaranteed to never need idle time, so return len(tasks).

        return max(len(tasks), (n+1) * (most_freq-1) + count_most_freq)
