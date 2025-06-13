class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        if(!p) return 0;
        sort(nums.begin(), nums.end());
        auto valid = [&](int threshold) {
            for(int i = 0, k = 0; i < nums.size() - 1; ++i) {
                if(nums[i+1] - nums[i] <= threshold) {
                    if(++k >= p) return true;
                    ++i;
                }
            }
            return false;
        };
        int lo = 0, hi = nums.back() - nums.front();
        while(lo < hi) {
            int m = lo + (hi - lo) / 2;
            if(valid(m)) {
                hi = m;
            } else {
                lo = m + 1;
            }
        }
        return lo;
    }
};
