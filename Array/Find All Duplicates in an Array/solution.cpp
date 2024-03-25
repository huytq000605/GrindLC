class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        std::vector<int> result;
        for(int i = 0; i < nums.size(); i++) {
            while(nums[i] != nums[nums[i] - 1]) {
                std::swap(nums[i], nums[nums[i] - 1]);
            }
        }
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] != i + 1) {
                result.push_back(nums[i]);
            }
        }
        
        return result;
    }
};
