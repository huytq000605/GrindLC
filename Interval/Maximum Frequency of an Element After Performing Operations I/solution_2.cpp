class Solution {
public:
    int maxFrequency(vector<int>& nums, int d, int numOperations) {
        sort(nums.begin(), nums.end());
        int result = 1;
        unordered_map<int, int> counter;
        // target is num in nums
        for(int i = 0, j = 0, k = 0; j < nums.size(); ++j) {
            while(nums[j] - nums[i] > d) ++i;
            while(k < nums.size() && nums[k] - nums[j] <= d) ++k;
            counter[nums[j]]++;
            result = max(result, min(k - i, counter[nums[j]] + numOperations));
        }
        // target is not in nums
        for(int i = 0, j = 0; i < nums.size(); ++i) {
            while(nums[j] + 2 * d < nums[i]) ++j;
            result = max(result, min(i - j + 1, numOperations));
        }
        return result;
    }
};
