class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size();
        // we can only remove subarray, so final array need to
        // start at arr[0] or end at arr[-1] or both
        // explore each case first and try to merge sorted prefix and sorted suffix
        int left{0};
        while(left+1 < n && arr[left] <= arr[left+1]) ++left;
        if(left==n-1) return 0;

        int right{n-1};
        while(right-1 >= 0 && arr[right] >= arr[right-1]) --right;
        int result = min(n-left-1, right);

        for(int i{0}; i <= left; ++i) {
            while(right+1 < n && arr[i] > arr[right]) {
                ++right;
            }
            if(arr[i] <= arr[right]) result = min(result, right - i - 1);
        }
        return result;
    }
};
