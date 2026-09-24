class Solution {
public:
    int minOperations(vector<int>& nums, long long x) {
        long long target = accumulate(begin(nums), end(nums), -x);
        unordered_map<long long, int> um;
        um[0] = -1;
        long long mx = -1;
        for(long long i = 0, s = 0; i < nums.size(); ++i) {
            long long num = nums[i];
            s += num;
            um[s] = i;
            if(um.find(s - target) != um.end()) {
                mx = max(mx, i - um[s-target]);
            }
            
        }
        return mx == -1 ? -1: nums.size() - mx;
    }
};
