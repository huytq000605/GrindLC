class Solution {
public:
    long long largestSquareArea(vector<vector<int>>& btm, vector<vector<int>>& top) {
        int n = btm.size();
        int mx = 0;
        for(int i = 0; i < n; ++i) {
            for(int j = i+1; j < n; ++j) {
                int r1x1 = btm[i][0], r1y1 = btm[i][1];
                int r1x2 = top[i][0], r1y2 = top[i][1];
                int r2x1 = btm[j][0], r2y1 = btm[j][1];
                int r2x2 = top[j][0], r2y2 = top[j][1];
                int l1 = min(r1x2, r2x2) - max(r1x1, r2x1);
                int l2 = min(r1y2, r2y2) - max(r1y1, r2y1);
                mx = max(mx, min(l1, l2));  
            }
        }
        return 1LL*mx*mx;
    }
};
