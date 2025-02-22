class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int n = nums.size();
        // select a subarray, add adjust all (x) to (k)
        // == find a subarray where freq(x) - freq(k) is maximized
        // then the max(freq(x)) = max_diff + freq(x)
        vector<int> count(51);
        int mx_diff{};
        for(int num: nums) {
            // if diff is < 0, we can just exclude them from selected subarray.
            count[num] = max(count[num], count[k]) + 1;
            mx_diff = max(mx_diff, count[num] - count[k]);
        }
        return count[k] + mx_diff;
    }
};
