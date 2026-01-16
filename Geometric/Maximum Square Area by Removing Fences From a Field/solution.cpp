class Solution {
public:
    int maximizeSquareArea(int m, int n, vector<int>& hs, vector<int>& vs) {
        sort(begin(hs), end(hs));
        sort(begin(vs), end(vs));
        hs.insert(hs.begin(), 1);
        hs.push_back(m);
        vs.insert(vs.begin(), 1);
        vs.push_back(n);
        unordered_set<int> sides;
        for(int i = 0; i < hs.size(); ++i) {
            for(int j = i+1; j < hs.size(); ++j) {
                sides.insert(hs[j] - hs[i]);
            }
        }
        int mx = 0;
        for(int i = 0; i < vs.size(); ++i) {
            for(int j = i+1; j < vs.size(); ++j) {
                int side = vs[j] - vs[i];
                if(sides.find(side) != sides.end()) {
                    mx = max(mx, side);
                }
            }
        }
        if(!mx) return -1;
        return 1LL*mx*mx%int(1e9+7);
    }
};
