class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        auto MOD = 1000000007;
        int s = accumulate(nums.begin(), nums.end(), 0);
        vector<int> prefix(n+1, 0);
        for(int i = 0; i < n; i++) {
            prefix[i+1] = prefix[i] + nums[i];
        }
        auto kth_sum = [&](auto k) {
            int low = 0;
            int high = s;
            while(low < high) {
                auto mid = low + (high - low) / 2;
                int count = 0;
                for(int i = 0, j = 0; i < n; i++) {
                    while(j < n && prefix[j+1] - prefix[i] <= mid) {
                        j++;
                    }
                    count += j - i;
                }
                if(count >= k) high = mid;
                else low = mid + 1;
            }
            return low;
        };
        vector<int> prefix_prefix(n+1, 0);
        for(int i = 0; i < n; i++) {
            prefix_prefix[i+1] = prefix_prefix[i] + prefix[i+1];
        }
        auto aggregate_k_sums = [&](auto k) {
            if(!k) return 0ll;
            int max_sum = kth_sum(k);
            long long agg = 0;
            int count = 0;
            for(int i = 0, j = 0; i < n; i++) {
                while(j < n && prefix[j+1] - prefix[i] <= max_sum) {
                    j++;
                }
                // sum of all subarrays start from [i] and ends at [i:j]
                // = (prefix[i+1] - prefix[i]) + (prefix[i+2] - prefix[i]) + ...
                // (prefix[j] - prefix[i])
                // = (prefix[i+1] + prefix[i+2] + ... prefix[j]) - prefix[i] * (j-i)
                // = (prefix_prefix[j] - prefix_prefix[i]) - prefix[i] * (j-i)
                agg += (prefix_prefix[j] - prefix_prefix[i]) - prefix[i] * (j-i);
                count += j - i;
            }
            return agg - (count - k) * max_sum;
        };
        return (aggregate_k_sums(right) - aggregate_k_sums(left-1)) % MOD;
    }
};
