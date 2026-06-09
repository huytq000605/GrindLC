class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        long long mn = *min_element(begin(nums), end(nums));
        long long mx = *max_element(begin(nums), end(nums));
        return (mx - mn) * k;
    }
};
