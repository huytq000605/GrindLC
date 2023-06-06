class Solution:
    def minOperations(self, n: int) -> int:
        group = []
        i = 0
        result = 0
        
        # Create group of ones
        # If group size is 1, remove it with 1 operation
        # If two groups are seperated by 1 zero, merge it with 1 operation (Not applied to above group)
        # group = [a, b] with a means index, b means group size is > 1
        while n:
            if n & 1:
                # same group
                if group and group[-1][0] == i-1:
                    group[-1] = [i, True]
                else:
                    # can merge group, check if is seperated by 1 zero and previous group size > 1
                    if group and group[-1][0] == i-2 and group[-1][1]:
                        result += 1
                        group[-1] = [i, True]
                    # new group
                    else:
                        group.append([i, False])
            i += 1
            n >>= 1

        for _, twice in group:
            if twice:
                result += 2
            else:
                result += 1
        return result
                
