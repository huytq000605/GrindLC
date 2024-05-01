class Solution {
public:
    long long countPairs(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        for(int i = 0; i < n; i++) {
            nums1[i] -= nums2[i];
        }
        sort(nums1.begin(), nums1.end());
        int j = n-1;
        long long result = 0;
        for(int i = 0; i < n; i++) {
            while(j > i && nums1[i] + nums1[j] > 0) {
                j -= 1;
            }
            result += n-max(i, j)-1;
        }
        return result;
    }
};
