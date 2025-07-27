class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int result = 0;
        for(int i = 1; i < nums.size(); ++i) {
            int left = i-1;
            while(i+1 < nums.size() && nums[i+1] == nums[i]) {
                i++;
            }
            int right = i+1;
            if(right >= nums.size()) break;
            if(nums[i] < nums[left] && nums[i] < nums[right]) result++;
            else if(nums[i] > nums[left] && nums[i] > nums[right]) result++;
        }
        return result;
    }
};
