class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int lo = 0, hi = nums.back() - nums.front();
        while(lo < hi) {
            int d = lo + (hi - lo) / 2;
            int j = 0, kth = 0;
            for(int i = 0; i < nums.size() - 1; i++) {
                j = upper_bound(nums.begin() + j, nums.end(), nums[i] + d) - nums.begin();
                kth += j - i - 1;
            }
            if(kth < k) lo = d + 1;
            else hi = d;
        }
        return lo;
    }
};
