class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, long long> m;
        m[k-1] = 0;
        long long result{LONG_MIN};
        long long s{};
        for(int i{}; i < nums.size(); ++i) {
            s += nums[i];
            if(m.find(i % k) != m.end()) {
                result = max(result, s - m[i % k]);
            }
            if(m.find(i%k) != m.end()) m[i%k] = min(m[i%k], s);
            else m[i%k] = s;
        }
        return result;
    }
};
