class Solution {
public:
    vector<int> distinctNumbers(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        vector<int> result;
        for(int i{}; i < nums.size(); ++i) {
            if(i >= k) {
                counter[nums[i-k]] -= 1;
                if(!counter[nums[i-k]]) counter.erase(nums[i-k]);
            }
            counter[nums[i]]++;
            if(i >= k-1) result.emplace_back(counter.size());
        }
        return result;
    }
};
