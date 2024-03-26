class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] <= 0 || nums[i] > nums.size()) {
                continue;
            }
            while(nums[i] > 0 && nums[i] <= nums.size() && nums[i] != nums[nums[i] - 1]) {
                std::swap(nums[i], nums[nums[i] - 1]);
            }
        }

        int result = 1;
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] != result) {
                return result;
            }
            result++;
        }
        return result;
    }
};
