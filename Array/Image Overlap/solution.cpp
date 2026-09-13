class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int n = img1.size();
        vector<pair<int, int>> i1, i2;
        for(int r = 0; r < n; ++r) {
            for(int c = 0; c < n; ++c) {
                if(img1[r][c]) i1.emplace_back(r, c);
                if(img2[r][c]) i2.emplace_back(r, c);
            }
        }
        vector<vector<int>> diff(2 * n, vector<int>(2 * n));
        int result = 0;
        for(auto [r1, c1]: i1) {
            for(auto [r2, c2]: i2) {
                diff[r1-r2+n][c1-c2+n]++;
                result = max(result, diff[r1-r2+n][c1-c2+n]);
            }
        }
        return result;
    }
};
