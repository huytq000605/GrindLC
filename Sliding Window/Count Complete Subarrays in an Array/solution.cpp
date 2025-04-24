class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int m = s.size();
        unordered_map<int, int> counter;
        int result = 0;
        for(int i = 0, j = 0; i < nums.size(); ++i) {
            counter[nums[i]]++;
            while(counter.size() == m) {
                if(--counter[nums[j]] == 0) {
                    counter.erase(nums[j]);
                }
                ++j;
            }
            result += j;
        }
        return result;
    }
};
