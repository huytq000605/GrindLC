class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        long long s1 = 0, s2 = 0;
        bool z1 = false, z2 = false;
        for(int num: nums1) {
            z1 |= num == 0;
            s1 += num ? num: 1;
        }
        for(int num: nums2) {
            z2 |= num == 0;
            s2 += num ? num: 1;
        }
        if(s1 < s2 && !z1) return -1;
        if(s2 < s1 && !z2) return -1;
        return max(s1, s2);
    }
};
