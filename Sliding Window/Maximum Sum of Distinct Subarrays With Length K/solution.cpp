class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long result{};
        long long s{};
        unordered_set<int> seen;
        for(int i{}, j{}; i < nums.size(); ++i) {
            while(j <= i - k || seen.find(nums[i]) != seen.end()) {
                seen.erase(nums[j]);
                s -= nums[j++];
            }
            seen.emplace(nums[i]);
            s += nums[i];
            if(i-j+1 == k) result = max(result, s);
        }
        return result;
    }
};
