class Solution {
public:
    long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
        long long result = 0;
        long long cnt = 0;
        unordered_map<int, int> seen;
        seen[0] = 1;
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] % modulo == k) {
                cnt = (cnt+1) % modulo;
            }
            result += seen[(cnt-k+modulo)%modulo];
            seen[cnt]++; 
        }
        return result;
    }
};
