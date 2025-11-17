class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        for(int i = 0, prev = -1e5; i < nums.size(); ++i) {
            if(nums[i]) {
                if(i - prev <= k) return false;
                prev = i;
            }
        }
        return true;
    }
};
