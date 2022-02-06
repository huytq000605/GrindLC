class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        for d in str(num):
            arr.append(int(d))
        arr.sort()
        return 10 * (arr[0] + arr[1]) + arr[2] + arr[3]