class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int result = 0;
        for(int i = 0, j = 0; i < nums1.size(); ++i) {
            while(j+1 < nums2.size() && nums2[j+1] >= nums1[i]) {
                j++;
            }
            result = max(result, j - i);
        }
        return result;
    }
};
