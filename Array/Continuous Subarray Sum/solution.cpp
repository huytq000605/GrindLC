class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        std::unordered_map<int, int> map;
        map[0] = -1;
        int s = 0;
        for(int i = 0; i < nums.size(); i++) {
            s += nums[i];
            s %= k;
            if(map.find(s) != map.end() && i - map.find(s)->second > 1) {
                return true;
            }
            if(map.find(s) == map.end()) map[s] = i;
        }
        return false;
    }
};
