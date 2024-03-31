class Solution {
public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        int bits[30];
        int o = 0;
        int result = INT_MAX;
        int start = 0;
        for(int i = 0; i < nums.size(); i++) {            
            int num = nums[i];
            int bit = 0;
            while(num) {
                if((num & 1) && !bits[bit]) o += 1 << bit;
                bits[bit] += num & 1;
                bit += 1;
                num >>= 1;
            }
            while(o >= k && start <= i) {
                result = min(result, i - start + 1);
                int num = nums[start];
                int bit = 0;
                while(num) {
                    bits[bit] -= num & 1;
                    if((num & 1) && !bits[bit]) o -= 1 << bit;
                    bit += 1;
                    num >>= 1;
                }
                start += 1;
            }
        }
        if(result == INT_MAX) return -1;
        return result;
    }
};
