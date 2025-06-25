class Solution {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        auto lte = [&](long long product) -> long long {
            long long result = 0;
            for(auto num1: nums1) {
                if(num1 > 0) {
                    long long target = floor(static_cast<double>(product) / num1);
                    result += upper_bound(nums2.begin(), nums2.end(), target) - nums2.begin();
                } else if(num1 == 0) {
                    result += product >= 0 ? static_cast<int>(nums2.size()): 0;
                } else {
                    long long target = ceil(static_cast<double>(product) / num1);
                    result += nums2.end() - lower_bound(nums2.begin(), nums2.end(), target);
                }
            }
            return result;
        };
        long long lo = -pow(10, 10);
        long long hi = pow(10, 10);
        while(lo < hi) {
            long long product = lo + (hi - lo) / 2;
            if(lte(product) < k) {
                lo = product + 1;
            } else {
                hi = product;
            }
        }
        return lo;
    }
};
