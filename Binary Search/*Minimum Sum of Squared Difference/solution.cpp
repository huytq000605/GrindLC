class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int n = nums1.size();
        int k = k1 + k2;
        int mx = max(*max_element(begin(nums1), end(nums1)),
                            *max_element(begin(nums2), end(nums2)));
        vector<int> nums(mx+1);
        for(int i = 0; i < n; i++) {
            nums[abs(nums1[i] - nums2[i])]++;
        }
        
        for(int i = mx; i && k; --i) {
            int d = min(k, nums[i]);
            nums[i] -= d;
            nums[i-1] += d;
            k -= d;
            mx = i;
        }
        long long result = 0;
        for(int i = mx; i >= 0; --i) {
            result += static_cast<long long>(nums[i]) * i * i;
        }
        return result;
    }
};
