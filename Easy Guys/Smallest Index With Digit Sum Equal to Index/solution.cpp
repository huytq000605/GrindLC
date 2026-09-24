class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        for(int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            int ds = 0;
            while(num && ds <= i) {
                ds += num % 10;
                num /= 10;
            }
            if(ds == i) return i;
        }
        return -1;
    }
};
