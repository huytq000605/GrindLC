class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int result = 0;
        for(int num: nums) {
            int res = 1;
            while(num) {
                num /= 10;
                res ^= 1;
            }
            result += res;
        }   
        return result;
    }
};
