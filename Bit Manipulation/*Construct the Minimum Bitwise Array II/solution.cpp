class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> result(nums.size(), -1);
        // num is all 1, the ans will be removing the msb
        // otherwise, the ans must contain the msb
        // removing msb from num and repeat the process
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] == 2) continue;
            int num = nums[i], res = 0;
            while(num) {
                if((num&(num+1)) == 0) { // is num+1 power of 2
                    res += num >> 1;
                    num = 0;
                } else {
                    int exp = floor(log2(num));
                    res += 1 << exp;
                    num -= 1 << exp;
                }
            }
            result[i] = res;
        }
        return result;
    }
};
