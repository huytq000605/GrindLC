class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, long long k) {
        // 6 2 4
        // If we iterate the vector forward in sliding window, we recognize that
        // we're in trouble whenever we pop out the front of the window, we cannot
        // keep track the cost, but if we iterate it backward, we found that whenever
        // we meet a new element, we can determine its cost thus when later popping it out
        // we can determine the cost to recover.
        // The key here is we could only increase elements but not decrease it.
        deque<int> dq;
        long long result{};
        // non-decreasing -> non-increasing when reverse
        reverse(nums.begin(), nums.end());
        for(int i{}, j{}; i < nums.size(); ++i) {
            // 6 1 2 2 4
            // i l r
            // i     l r
            // i   l   r
            while(!dq.empty() && nums[i] > nums[dq.back()]) {
                int r = dq.back(); 
                dq.pop_back();
                int l = dq.empty() ? j-1: dq.back();
                k -= 1ll * (r-l) * (nums[i] - nums[r]);
            }
            dq.emplace_back(i);
            while(k < 0) {
                k += nums[dq.front()] - nums[j];
                if(j == dq.front()) dq.pop_front();
                ++j;
            }
            result += i-j+1;
        }

        return result;
    }
};
