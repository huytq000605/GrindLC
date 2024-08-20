class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        deque<int> window;
        vector<int> result(nums.size() - k + 1, -1);
        for(int i = 0, j = 0; i < nums.size(); ++i) {
            if(!window.empty() && window.back() + 1 != nums[i]) {
                window.clear();
            }
            window.emplace_back(nums[i]);
            if(window.size() > k) window.pop_front();
            if(window.size() == k) result[i-k+1] = window.back();
        }
        return result;
    }
};
