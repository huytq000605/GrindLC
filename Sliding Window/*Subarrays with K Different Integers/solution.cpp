class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        auto at_most = [&](int k) {
            unordered_map<int, int> counter;
            int start = 0, result = 0;
            for(int i = 0; i < nums.size(); i++) {
                counter[nums[i]]++;
                while(counter.size() > k) {
                    counter[nums[start]]--;
                    if(!counter[nums[start]]) counter.erase(nums[start]);
                    start++;
                }
                result += (i - start + 1);
            }
            return result;
        };
        return at_most(k) - at_most(k-1);
    }
};
