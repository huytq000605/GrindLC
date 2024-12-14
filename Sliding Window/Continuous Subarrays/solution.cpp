class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        unordered_map<int, int> m;
        long long result{};
        auto valid = [&](int num) -> bool {
            for(auto &[other, freq]: m) {
                if(abs(num - other) > 2) {
                    return false;
                }
            }
            return true;
        };
        for(int i{}, j{}; i < nums.size(); ++i) {
            while(!valid(nums[i])) {
                --m[nums[j]];
                if(!m[nums[j]]) m.erase(nums[j]);
                ++j;
            }
            ++m[nums[i]];
            result += (i - j + 1);
        }
        return result;
    }
};
