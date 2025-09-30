int ncr[1001][1001] = {}, n = 0;

class Solution {
public:
    int triangularSum(vector<int>& nums) {
        // 1 2 3 4 5
        // (1+2) + (2+3) + (3+4) + (4+5)
        // (1+2+2+3) + (2+3+3+4) + (3+4+4+5)
        // (1+2+2+2+3+3+3+4) + (2+3+3+3+4+4+4+5)
        // 1 1 1 1 1 
        // 1 2 2 2 1
        // 1 3 4 3 1
        // 1 4 6 4 1
        for(; n <= nums.size(); ++n) {
            for(int r = 0; r <= n; ++r) {
                ncr[n][r] = r == 0 ? 1: (ncr[n-1][r] + ncr[n-1][r-1]) % 10;
            }
        }
        int result = 0;
        for(int i = 0; i < nums.size(); ++i) {
            result = (result + nums[i] * ncr[nums.size()-1][i]) % 10;
        }
        return result;
    }
};
