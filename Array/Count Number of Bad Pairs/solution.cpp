class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        int n = nums.size();
        long long good_pairs{};
        long long total_choices{static_cast<long long>(n) * (n-1) / 2};
        unordered_map<int, int> m;
        for(int i{}; i < n; ++i) {
            good_pairs += m[i-nums[i]];
            m[i-nums[i]]++;
        }
        return total_choices - good_pairs;
    }
};
