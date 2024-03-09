from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
            arr1, arr2 = [nums[0]], [nums[1]]
            sl1, sl2 = SortedList(arr1), SortedList(arr2)
            def greaterCount(sl, num):
                i = sl.bisect_right(num)
                return len(sl) - i + 1
                
                
            for num in nums[2:]:
                c1, c2 = greaterCount(sl1, num), greaterCount(sl2, num)
                if c1 > c2:
                    arr1.append(num)
                    sl1.add(num)
                elif c1 < c2:
                    arr2.append(num)
                    sl2.add(num)
                else:
                    if len(arr1) <= len(arr2):
                        arr1.append(num)
                        sl1.add(num)
                    else:
                        arr2.append(num)
                        sl2.add(num)
            return arr1 + arr2
