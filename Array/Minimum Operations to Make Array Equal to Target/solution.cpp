class Solution {
public:
    long long minimumOperations(vector<int>& nums, vector<int>& target) {
        int n = nums.size();
        for(int i = 0; i < n; ++i) {
            nums[i] -= target[i];
        }
        
        long long incr = 0, decr = 0;
        long long result = 0;
        for(long long diff : nums) {
            if(diff > 0) {
                decr = 0;
                if(diff > incr) result += diff - incr;
                incr = diff;
            } else if(diff < 0) {
                incr = 0;
                diff = -diff;
                if(diff > decr) result += diff - decr;
                decr = diff;
            } else {
                incr = decr = 0;
            }
        }
        return result;
    }
};
