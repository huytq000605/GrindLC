from functools import cache

MOD = 10**9 + 7
@cache
def fact(n):
    if n < 2:
        return 1
    return (n * fact(n-1))% MOD

@cache
def ifact(n):
    return pow(fact(n), -1, MOD)

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        m = len(sick)
        # considering all the continuous healthy kids as a group
        # 
        # 1. infection process of each group
        # the first and the last group can only be infected from one side
        # -> 1 way
        # the remaining groups on each second can either be infected from the left or the right
        # -> 2 ** (group_length - 1) ways, the last person only has 1 way
        # 2. infection process between all groups
        # because each second, only 1 kid can be infected
        # that means on each second, we can choose any group
        # -> For each group, we have to put `group_length` into n positions
        # -> nCk1 * (n-k1)Ck2 * (n-k1-k2)Ck3 * ...
        # -> n! / (n-k1)! / k1! * (n-k1)! / k2! / (n-k1-k2)! * ...
        # -> n! / k1! / k2! / k3! /...
        result = fact(n-m) * ifact(sick[0]) * ifact(n-sick[-1]-1)
        result %= MOD
        for i in range(m - 1):
            if sick[i+1] - sick[i] > 1:
                group = sick[i+1] - sick[i] - 1
                result *= pow(2, group - 1, MOD)
                result %= MOD
                result *= ifact(group)
                result %= MOD
        return result
        

            
