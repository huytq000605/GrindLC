class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        auto is_magic = [&](int r, int c) -> bool {
            // [0, 3] for rows, [3, 6] for cols, 7 for dia1, 8 for dia2
            vector<int> vs(8, 0);
            vector<int> counter(10, 0);
            for(int dr = 0; dr < 3; dr++) {
                for(int dc = 0; dc < 3; dc++) {
                    int v = grid[r + dr][c + dc];
                    if(v < 1 || v > 9) return false;
                    counter[v]++;
                    if(counter[v] > 1) return false;
                    vs[dr] += v;
                    vs[3 + dc] += v;
                    if(dr == dc) vs[6] += v;
                    if(dr + dc == 2) vs[7] += v;
                }
            }
            return std::equal(vs.begin() + 1, vs.end(), vs.begin());
        };
        int result = 0;
        for(int r = 0; r < m - 2; r++) {
            for(int c = 0; c < n - 2; c++) {
                if(is_magic(r, c)) {
                    result++;
                }
            }
        }
        return result;
    }
};
