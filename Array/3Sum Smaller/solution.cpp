class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int result = 0;
        for(int i = 0; i < n-2; ++i) {
            for(int j = i+1, k = n-1; j < k; ++j) {
                while(k > j && nums[i] + nums[j] + nums[k] >= target) --k;
                result += k - j;
            }
        }
        return result;
    }
};
