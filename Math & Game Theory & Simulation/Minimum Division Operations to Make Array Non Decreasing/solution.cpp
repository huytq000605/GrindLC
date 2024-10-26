class Solution {
public:
    int minOperations(vector<int>& nums) {
        int result = 0;
        for(int i = nums.size()-2; i >= 0; --i) {
            if(nums[i] > nums[i+1]) {
                ++result;
                bool valid = false;
                for(int j = 2; j * j <= nums[i] && j <= nums[i+1]; ++j) {
                    if(nums[i] % j == 0) {
                        valid = true;
                        nums[i] = j;
                        break;
                    }
                }
                if(!valid) return -1;
            }
        }
        return result;
    }
};
