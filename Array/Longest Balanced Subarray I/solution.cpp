class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();
        int result = 0;
        for(int l = 0; l < n; ++l) {
            unordered_set<int> s;
            vector<int> counter(2, 0);
            for(int r = l; r < n; ++r) {
                if(s.find(nums[r]) == s.end()) {
                    s.emplace(nums[r]);
                    counter[nums[r] & 1]++;
                }
                if(counter[0] == counter[1]) result = max(result, r - l + 1);
            }
        }
        return result;
    }
};
