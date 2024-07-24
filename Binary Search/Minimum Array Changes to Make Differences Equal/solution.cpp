class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        // [a, b] with b > a
        // [0, b]
        // [0, k-b]
        // [0, k-a]
        // [0, a]
        // => [0, max(b, k-a)] is the possible range with 1 changes
        int n = nums.size();
        vector<int> thresholds(n/2);
        vector<int> diffs(k+1);
        for(int i = 0; i < n / 2; i++) {
            int b = max(nums[i], nums[n-1-i]);
            int a = min(nums[i], nums[n-1-i]);
            thresholds[i] = max(b, k - a);
            diffs[abs(nums[i] - nums[n-1-i])] += 1;
        }
        int result = n/2;
        sort(thresholds.begin(), thresholds.end());
        for(int target = 0; target <= k; target++) {
            // no need to change
            int rest = n/2 - diffs[target];
            // we are gonna need 1 change for rest
            // now we need to find in these rest, which pair we need to change both
            int both = lower_bound(thresholds.begin(), thresholds.end(), target) - thresholds.begin();
            result = min(result, both + rest);
        }
        return result;   
    }
};
