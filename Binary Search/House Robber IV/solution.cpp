class Solution {
public:
    int minCapability(vector<int>& nums, int k) {
        int lo = *min_element(nums.begin(), nums.end()), hi = *max_element(nums.begin(), nums.end());
        while(lo < hi) {
            int m = lo + (hi - lo) / 2;
            int houses = 0;
            for(int i = 0; i < nums.size(); ++i) {
                if(nums[i] <= m) {
                    ++i;
                    ++houses;
                }
            }
            if(houses >= k) {
                hi = m;
            } else {
                lo = m + 1;
            }
        }
        return lo;
    }
};
