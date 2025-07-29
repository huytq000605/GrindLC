class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        vector<int> last(32, -1);
        vector<int> result(nums.size(), 1);
        for(int i = nums.size() - 1; i >= 0; --i) {
            for(int bit = 0; bit < 32; ++bit) {
                if((nums[i] >> bit) & 1) last[bit] = i;
                result[i] = max(result[i], last[bit] - i + 1);
            }
        }
        return result;
    }
};
