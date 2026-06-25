class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();

        // Map each num to +1 if it equals target, else -1.
        // A subarray [l, r] has 'target' as a strict majority element
        // if prefixSum(r+1) - prefixSum(l) > 0, i.e. prefixSum(r+1) > prefixSum(l).
        // So for each prefix index, we need to count how many *earlier*
        // prefix values were strictly smaller than it.

        // cur is the offset-encoded current prefix sum: cur = n + prefixSum,
        // so it always stays in [0, 2n] and can index directly into count[].
        int cur = n;

        // count[v] = how many prefix sums seen so far are encoded as v.
        // Start with prefixSum(0) = 0 already "seen" (encoded as n).
        vector<int> count(2 * n + 1);
        count[n] = 1;

        // acc = number of previously seen prefix sums strictly less than
        // the CURRENT prefix sum (i.e. less than cur, in encoded terms).
        // We maintain this incrementally rather than recomputing a range
        // sum every iteration, which is possible because cur only ever
        // changes by exactly +1 or -1 per step.
        int acc = 0;
        long long result = 0;

        for (int num : nums) {
            if (num == target) {
                // New prefix sum = cur + 1.
                // Every old prefix that was < cur is still < cur+1.
                // Additionally, every old prefix that was == cur (there are
                // count[cur] of them) is now also < cur+1, since cur+1 > cur.
                // So fold those in BEFORE bumping cur.
                acc += count[cur];
                cur += 1;
            } else {
                // New prefix sum = cur - 1.
                // Move cur down first: now any old prefix equal to the NEW
                // cur (== old cur - 1) is no longer strictly less than the
                // new prefix sum, so it must be removed from acc.
                cur -= 1;
                acc -= count[cur];
                
            }
            // Record this new prefix sum in the histogram.
            count[cur]++;

            // acc now equals the number of earlier prefix sums strictly
            // less than the prefix sum ending at the current index, i.e.
            // the number of valid left endpoints l for this right endpoint.
            // Add that to the total count of majority subarrays.
            result += acc;
        }

        return result;
    }
};
