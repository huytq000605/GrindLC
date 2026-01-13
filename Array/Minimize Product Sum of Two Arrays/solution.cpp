class Solution {
public:
    int minProductSum(vector<int>& nums1, vector<int>& nums2) {
        int result = 0;
        vector<int> c1(101), c2(101);
        for(int num: nums1) c1[num]++;
        for(int num: nums2) c2[num]++;
        for(int i = 1, j = 100, k = 0; k < nums1.size();) {
            while(!c1[i]) ++i;
            while(!c2[j]) --j;
            int c = min(c1[i], c2[j]);
            result += i * j * c;
            c1[i] -= c;
            c2[j] -= c;
            k += c;
        }
        return result;
    }
};
