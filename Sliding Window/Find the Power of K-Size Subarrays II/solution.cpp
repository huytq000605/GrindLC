class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> result(n-k+1, -1);
        int consecutive{0};
        for(int i{0}; i < n; ++i) {
            if(i == 0 || nums[i] == nums[i-1] + 1) {
                consecutive++;
            } else {
                consecutive = 1;
            }
            if(i >= k -1 && consecutive >= k) result[i-k+1] = nums[i];
        }
        return result;
    }
};
