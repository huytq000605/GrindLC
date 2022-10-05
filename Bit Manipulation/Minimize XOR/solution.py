class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1, n2 = num1.bit_count(), num2.bit_count()
        if n1 == n2:
            result = num1
        elif n1 < n2:
            result = num1
            set_bit = n2 - n1
            for i in range(30):
                if (result >> i) & 1 == 0:
                    result += 1<<i
                    set_bit -= 1
                    if set_bit == 0:
                        break 
        else:
            result = num1
            not_set = n1 - n2
            for i in range(30):
                if (result >> i) & 1:
                    result -= 1 << i
                    not_set -= 1
                    if not_set == 0:
                        break
        return result
