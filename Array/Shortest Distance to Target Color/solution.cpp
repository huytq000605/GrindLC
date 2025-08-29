class Solution {
public:
    vector<int> shortestDistanceColor(vector<int>& colors, vector<vector<int>>& queries) {
        // O(n)
        int n = colors.size();
        vector<vector<int>> left(4, vector<int>(n)), right(4, vector<int>(n));
        for(int color = 1; color <= 3; ++color) {
            left[color][0] = colors[0] == color ? 0: -1;
            for(int i = 1; i < n; ++i) {
                if(color == colors[i]) {
                    left[color][i] = 0;
                } else {
                    left[color][i] = left[color][i-1] != -1 ? left[color][i-1] + 1: -1;
                }
            }

            right[color][n-1] = colors[n-1] == color ? 0: -1;
            for(int i = n - 2; i >= 0; --i) {
                if(color == colors[i]) {
                    right[color][i] = 0;
                } else {
                    right[color][i] = right[color][i+1] != -1 ? right[color][i+1] + 1: -1;
                }
            }
        }
        vector<int> result;
        for(auto &q: queries) {
            int i = q[0], c = q[1];
            int l = left[c][i];
            int r = right[c][i];
            if(l == -1 || r == -1) {
                result.push_back(max(l, r));
            } else {
                result.push_back(min(l, r));
            }
        }
        return result;


        // O(nlog(n))
        // vector<vector<int>> idxs(3);
        // for(int i = 0; i < colors.size(); ++i) {
        //     idxs[colors[i]-1].push_back(i);
        // }
        // vector<int> result;
        // for(auto &q: queries) {
        //     int i = q[0], c = q[1];
        //     if(idxs[c-1].empty()) result.push_back(-1);
        //     else {
        //         int j = lower_bound(idxs[c-1].begin(), idxs[c-1].end(), i) - idxs[c-1].begin();
        //         int d = min(j > 0 ? i - idxs[c-1][j-1]: INT_MAX, j < idxs[c-1].size() ? idxs[c-1][j] - i: INT_MAX);
        //         result.push_back(d);
        //     }
        // }
        // return result;
    }
};
