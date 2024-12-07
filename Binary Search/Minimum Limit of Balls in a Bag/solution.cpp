class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        int lo{1}, hi{*max_element(nums.begin(), nums.end())};
        while(lo < hi) {
            int mi = lo + (hi - lo) / 2;
            int ops{};
            bool valid{true};
            for(int num: nums) {
                ops += (num + mi - 1) / mi - 1;
                if(ops > maxOperations) {
                    valid = false;
                    break;
                }
            }
            if(valid) hi = mi;
            else lo = mi + 1;
        }
        return lo;
    }
};
