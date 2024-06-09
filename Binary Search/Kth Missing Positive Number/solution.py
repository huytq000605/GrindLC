class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr)
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] - mid - 1 < k: # no of missing number < k
                start = mid + 1
            else:
                end = mid
        # start is the smallest index that no of missing numbers is (arr[start] - start - 1) >= k
        # since it can contain more than k missing numbers
        # => between arr[start-1] and arr[start], there must be kth missing number
        # arr[start-1] has (arr[start-1] - (start-1) - 1) missing numbers
        # need to find k - (arr[start-1] - (start-1) - 1) missing numbers in between
        # num at start - 1 is arr[start - 1]
        # => k-th missing number is: arr[start-1] + (k - arr[start-1] + start) = start + k
        return start + k
