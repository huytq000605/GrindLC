# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        start = 0
        end = reader.length() - 1
        while start < end:
            mid = start + (end - start) // 2
            if (end - start + 1) % 2 == 1:
                cmp = reader.compareSub(start, mid-1, mid + 1, end)
            else:
                cmp = reader.compareSub(start, mid, mid+1, end)
            
            if cmp == -1:
                start = mid+1
            else:
                end = mid
        return start
