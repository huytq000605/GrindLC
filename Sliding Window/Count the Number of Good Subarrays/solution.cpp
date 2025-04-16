class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        long long result = 0;
        unordered_map<int, int> counter;
        int pairs = 0;
        for(int i = 0, j = 0; i < nums.size(); ++i) {
            pairs += counter[nums[i]]++;
            while(pairs >= k) {
                pairs -= --counter[nums[j++]];
            }
            result += j;
        }
        return result;
    }
};
