class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping_map = dict()
        for i in range(len(mapping)):
            mapping_map[i] = mapping[i]
        new_nums = []
        for idx, num in enumerate(nums):
            new_num = 0
            for d in str(num):
                digit = int(d)
                new_digit = mapping_map[digit]
                new_num = new_num * 10 + new_digit
            new_nums.append((new_num, idx, num))
        
        result = [num[2] for num in sorted(new_nums)]
        return result