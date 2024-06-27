class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long long can = 0;
        int i = 0;
        int result = 0;
        while(can < n) {
            if(i < nums.size() && nums[i] <= can + 1) {
                can += nums[i++];
            } else {
                result += 1;
                can += can + 1;
            }
        }
        return result;
    }
};
