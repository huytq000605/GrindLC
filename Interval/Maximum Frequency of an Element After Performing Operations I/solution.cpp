class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        sort(nums.begin(), nums.end());
        int result = 0;
        unordered_map<int, int> counter{};
        for(int num: nums) ++counter[num];
        for(int target{nums.front() - k}; target <= nums.back() + k; ++target) {
            auto a = lower_bound(nums.begin(), nums.end(), target - k);
            auto b = lower_bound(nums.begin(), nums.end(), target + k + 1);
            result = max(result, min(static_cast<int>(b-a), (counter.find(target) != counter.end() ? counter[target] : 0) + numOperations));
        }
        return result;
    }
};
