class FrequencyTracker:

    def __init__(self):
        self.counter = defaultdict(int)
        self.freq_counter = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq_counter[self.counter[number]] -= 1
        self.counter[number] += 1
        self.freq_counter[self.counter[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.counter:
            self.freq_counter[self.counter[number]] -= 1
            self.counter[number] -= 1
            self.freq_counter[self.counter[number]] += 1
            if not self.counter[number]: 
                self.counter.pop(number)

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq_counter and self.freq_counter[frequency]:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
