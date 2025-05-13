class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();
        if(n <= 2) return n;
        int result = 1;
        while(n) {
            result <<= 1;
            n >>= 1;
        }
        return result;
    }
};
