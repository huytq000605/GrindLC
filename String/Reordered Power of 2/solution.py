class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def num_to_counter(num):
            counter = Counter()
            while num > 0:
                counter[num%10] += 1
                num //= 10
            return counter

        counter = num_to_counter(n)
        num = 1
        while num <= 10**9:
            counter_num = num_to_counter(num)
            valid = True
            for i in range(10):
                if counter[i] != counter_num[i]:
                    valid = False
                    break
            if valid:
                return True
            num *= 2
        return False
