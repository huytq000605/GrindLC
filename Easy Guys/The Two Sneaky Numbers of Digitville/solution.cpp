class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        std::vector<int> result;
        for(int i = 0; i < nums.size(); i++) {
            while(nums[i] != nums[nums[i]]) {
                std::swap(nums[i], nums[nums[i]]);
            }
        }
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] != i) {
                result.push_back(nums[i]);
            }
        }
        
        return result;
    }
};
