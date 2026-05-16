class Solution {
public:
    int findMin(vector<int>& nums) {
        auto find = [&](this auto& find, int lo, int hi) -> int {
            if(lo > hi) return INT_MAX;
            if(nums[lo] < nums[hi]) return nums[lo];
            while(lo < hi) {
                int mi = lo + (hi - lo) / 2;
                if(nums[mi] < nums[0]) {
                    hi = mi;
                } else if(nums[mi] > nums[0]) {
                    lo = mi + 1;
                } else {
                    return min(find(lo, mi), find(mi+1, hi));
                }
            }
            return nums[lo];
        };
        return find(0, nums.size() - 1);
    }
};
