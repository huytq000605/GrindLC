class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int result = 0;
        for(int num: nums) {
            result += num % 3 ? 1: 0;
        }
        return result;
    }
};
