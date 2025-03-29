class Solution {
public:
    int shortestWay(string source, string target) {
        int n = source.size(), m = target.size();
        vector<vector<int>> idxs(26);
        for(int i = 0; i < n; ++i) {
            int c = source[i] - 'a';
            idxs[c].emplace_back(i);
        }
        int result = 1;
        for(int i = 0, j = 0; i < m; i++) {
            int c = target[i] - 'a';
            if(idxs[c].empty()) return -1;
            auto next_j_pos = lower_bound(idxs[c].begin(), idxs[c].end(), j);
            if(next_j_pos == idxs[c].end()) {
                ++result;
                next_j_pos = idxs[c].begin();
            }
            j = idxs[c][next_j_pos - idxs[c].begin()] + 1;
        }
        return result;
    }
};
