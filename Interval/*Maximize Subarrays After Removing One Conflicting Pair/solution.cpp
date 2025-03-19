class Solution {
public:
    long long maxSubarrays(int n, vector<vector<int>>& pairs) {
        vector<vector<int>> rights(n+1);
        for(auto &pair: pairs) {
            int l = min(pair[0], pair[1]);
            int r = max(pair[0], pair[1]);
            rights[r].emplace_back(l);
        }
        vector<long long> better_lefts(n+1);
        pair<int, int> top2_left{0, 0};
        long long result = 0;
        for(int r = 1; r <= n; ++r) {
            for(auto l: rights[r]) {
                top2_left.second = max(top2_left.second, l);
                if(top2_left.second > top2_left.first) {
                    top2_left = {top2_left.second, top2_left.first};
                }
            }
            result += r - top2_left.first;
            better_lefts[top2_left.first] += (top2_left.first - top2_left.second);
        }
        return result + *max_element(better_lefts.begin(), better_lefts.end());
    }
};
