class Solution {
public:
    int numTilePossibilities(string tiles) {
        set<string> possible;
        int n = tiles.size();
        string s{};
        auto dfs = [&](this auto& dfs, int mask) {
            possible.emplace(s);
            if(mask == ((1<<n) - 1)) {
                return;
            }
            for(int i{}; i < n; ++i) {
                if(!((mask >> i) & 1)) {
                    s += tiles[i];
                    dfs(mask | (1 << i));
                    s.pop_back();
                }
            }
        };
        dfs(0);
        return possible.size()-1;
    }
};
