class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        if(nums[0] < nums[n-1]) return nums[0];
        int lo = 0, hi = n-1;
        while(lo < hi) {
            int mi = lo + (hi - lo) / 2;
            if(nums[mi] < nums[0]) {
                hi = mi;
            } else {
                lo = mi+1;
            }
        }
        return nums[lo];
    }
};
