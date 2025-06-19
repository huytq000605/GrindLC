class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        int mx = *max_element(nums.begin(), nums.end());
        vector<bool> exists(mx+1);
        int prev = INT_MAX;
        for(int &num: nums) {
            exists[num] = true;
            prev = min(prev, num);
        }
        int result = 1;
        for(int num = 0; num <= mx; ++num) {
            if(!exists[num]) continue;
            if(num - prev > k) {
                prev = num;
                ++result;
            }
        }
        return result;
    }
};
