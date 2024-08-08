class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int m, int n, int r, int c) {
        vector<vector<int>> result;
        int need = m*n;
        int threshold = 1;
        auto add = [&](int r, int c) {
            if(r >= 0 && r < m && c >= 0 && c < n) {
                need--;
                result.push_back({r, c});
            }
        };
        add(r, c);
        while(need > 0) {
            for(int i = 0; i < threshold && need > 0; i++) {
                c++;
                add(r, c);
            }
            for(int i = 0; i < threshold && need > 0; i++) {
                r++;
                add(r, c);
            }
            threshold++;
            for(int i = 0; i < threshold && need > 0; i++) {
                c--;
                add(r, c);
            }
            for(int i = 0; i < threshold && need > 0; i++) {
                r--;
                add(r, c);
            }
            threshold++;
        }
        return result;
    }
};
