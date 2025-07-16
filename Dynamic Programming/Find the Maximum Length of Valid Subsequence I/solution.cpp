class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int odd = 0, even = 0, alternate = 0;
        int looking = nums[0] & 1;
        for(int num: nums) {
            odd += num & 1;
            even += !(num & 1);
            alternate += looking == (num & 1);
            looking = 1 - (num & 1);
        }

        return max({odd, even, alternate});
    }
};
