class Solution {
    int reverse(int num) {
        int result = 0;
        while(num) {
            result = (result * 10) + num % 10;
            num /= 10;
        }
        return result;
    }
public:
    int minMirrorPairDistance(vector<int>& nums) {
        unordered_map<int, int> um;
        int result = INT_MAX;
        for(int i = 0; i < nums.size(); ++i) {
            if(um.find(nums[i]) != um.end()) {
                result = min(result, i - um[nums[i]]);
            }
            int rnum = reverse(nums[i]);
            um[rnum] = i;
        }
        if(result == INT_MAX) return -1;
        return result;
    }
};
