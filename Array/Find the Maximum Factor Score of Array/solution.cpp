class Solution {
public:
    long long maxScore(vector<int>& nums) {
        long long result = 0;
        for(int skip = -1; skip < static_cast<int>(nums.size()); ++skip) {
            long long g = 0;
            long long l = 0;
            for(int i = 0; i < nums.size(); ++i) {
                if(i == skip) continue;
                if(!g) {
                    g = nums[i];
                    l = nums[i];
                } else {
                    g = gcd(g, nums[i]);
                    l = lcm(l, nums[i]);
                }
            }
            result = max(result, g * l);
        }
        return result;
    }
};
