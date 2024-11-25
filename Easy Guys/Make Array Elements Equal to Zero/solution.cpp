class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int s = accumulate(nums.begin(), nums.end(), 0);
        int prefix{};
        int result{};
        for(int num: nums) {
            if(!num) {
                if(prefix == s - prefix) result += 2;
                else if(abs(s - 2 * prefix) == 1) result += 1;
            }
            
            prefix += num;
        }
        return result;
    }
};
