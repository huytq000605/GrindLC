class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        function<long long(int k)> lte = [&](int k) {
            long long result{};
            for(int i{}, j{n-1}; i < n; ++i) {
                while(j > i && nums[i] + nums[j] > k) --j;
                if(j == i) break;
                result += max(0, j-i);
            }
            return result;
        };
        return lte(upper) - lte(lower-1);
    }
};
