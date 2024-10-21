class Solution {
vector<int> nums;
public:
    Solution(vector<int>& nums) {
       this->nums = nums; 
    }
    
    int pick(int target) {
        // p(i) = p_select(i) * p_keep(i)
        // p(1) = 1 * 1/2 * 2/3 * 3/4 * ... * (n-1)/n = 1/n
        // p(2) = 1/2 * 2/3 * ... 
        int n = 0;
        int result = -1;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] != target) continue;
            if(rand() % ++n == 0) result = i; 
        }
        return result;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
