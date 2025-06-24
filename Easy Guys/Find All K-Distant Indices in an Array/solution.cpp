class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        int n  = nums.size();
        vector<int> result;
        for(int i = 0, j = 0; i < n; ++i) {
            if(nums[i] == key) {
                j = max(j, i - k);
                for(; j <= min(i+k, n-1); ++j) {
                    result.emplace_back(j);
                }
            }
        }
        return result;
    }
};
