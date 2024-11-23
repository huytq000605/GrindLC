class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m = box.size(), n = box[0].size();
        vector<vector<char>> result(n, vector<char>(m, '.'));
        for(int r{}; r < m; ++r) {
            int rr = n-1;
            for(int c{n-1}; c >= 0; --c) {
                if(box[r][c] == '*') {
                    result[c][m-1-r] = '*';
                    rr = c-1;
                } else if(box[r][c] == '#') {
                    result[rr--][m-1-r] = '#';
                }
            }
        }
        return result;
    }
};
