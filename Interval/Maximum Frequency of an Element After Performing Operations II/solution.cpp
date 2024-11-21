class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        int result{0};
        sort(nums.begin(), nums.end());
        unordered_map<int, int> counter;
        for(int num: nums) counter[num]++;
        for(int num: nums) {
            for(long long target: {num - k, num, num + k}) {
                int total = upper_bound(nums.begin(), nums.end(), target + k) - lower_bound(nums.begin(), nums.end(), target - k);
                int count = counter.find(target) == counter.end() ? 0: counter[target];
                result = max(result, count + min(total - count, numOperations));
            }
        }
        return result;
    }
};
