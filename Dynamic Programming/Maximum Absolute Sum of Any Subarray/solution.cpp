class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int mx{}, mn{}, result{};
        for(int num: nums) {
            mx = max(mx + num, num);
            mn = min(mn + num, num);
            result = max({result, -mn, mx});
        }
        return result;
    }
};
