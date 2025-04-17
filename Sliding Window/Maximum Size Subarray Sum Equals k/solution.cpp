class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        int result = 0;
        unordered_map<long long, int> seen;
        seen[0] = -1;
        long long s = 0;
        for(int i = 0; i < nums.size(); ++i) {
            s += nums[i];
            if(seen.find(s-k) != seen.end()) {
                result = max(result, i - seen[s-k]);
            }
            if(seen.find(s) == seen.end()) seen[s] = i;
        }
        return result;
    }
};
