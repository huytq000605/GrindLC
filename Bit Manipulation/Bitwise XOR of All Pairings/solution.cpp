class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int result{};
        int n = nums1.size(), m = nums2.size();
        if(m & 1)
            for(int num: nums1) {
                result ^= num;
            }
        if(n & 1)
            for(int num: nums2) {
                result ^= num;
            }
        return result;
    }
};
