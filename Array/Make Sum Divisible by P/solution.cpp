class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int mod = 0;
        for(int num: nums) {
            mod = (mod + num) % p;
        }
        int result = nums.size();
        unordered_map<int, int> seen;
        seen[0] = -1;
        int s = 0;
        for(int i = 0; i < nums.size(); ++i) {
            s = (s + nums[i]) % p;
            seen[s] = i;
            int need  = (s - mod + p) % p;
            if(seen.find(need) != seen.end()) {
                result = min(result, i - seen[need]);
            }   
        }
        if(result == nums.size()) return -1;
        return result;
    }
};
