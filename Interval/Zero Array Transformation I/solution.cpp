class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> prefix(nums.size()+1, 0);
        for(auto &query: queries) {
            ++prefix[query[0]];
            --prefix[query[1] + 1];
        }
        int cur{};
        for(int i{}; i < nums.size(); ++i) {
            cur += prefix[i];
            nums[i] -= cur;
            if(nums[i] > 0) return false;
        }
        return true;
    }
};
