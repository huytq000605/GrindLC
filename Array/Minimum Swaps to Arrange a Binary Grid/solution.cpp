class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> rows(n);
        for(int r = 0; r < n; ++r) {
            for(int c = n-1; c >= 0; --c) {
                if(grid[r][c]) break;
                rows[r] += 1;
            }
        }
        int result = 0;
        for(int r = 0, expected = n-1; r < n; ++r, expected--) {
            if(rows[r] < expected) {
                int nr = r + 1;
                while(nr < n && rows[nr] < expected) ++nr;
                if(nr == n) return -1;
                while(nr > r) {
                    swap(rows[nr], rows[nr-1]);
                    --nr;
                    ++result;
                }
            }
        }
        return result;
    }
};
