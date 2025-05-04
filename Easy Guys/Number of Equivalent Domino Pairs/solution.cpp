class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        vector<vector<int>> seen(10, vector<int>(10, 0));
        int result = 0;
        for(auto &d: dominoes) {
            int mn = min(d[0], d[1]);
            int mx = max(d[0], d[1]);
            result += seen[mn][mx]++;
        }
        return result;
    }
};
