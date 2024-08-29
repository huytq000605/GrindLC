class UF {
    public:
    unordered_map<int, int> p;
    unordered_map<int, int> r;

    int find(int u) {
        if(p.find(u) == p.end()) p[u] = u;
        if(u != p[u]) {
            p[u] = find(p[u]);
        }

        return p[u];
    }

    void uni(int u, int v) {
        u = find(u);
        v = find(v);
        if(u == v) return;
        if(r[u]< r[v]) {
            swap(u, v);
        }
        r[u] += r[v];
        p[v] = u;
    }
};

class Solution {
    static constexpr int OFFSET = 10001;

public:
    int removeStones(vector<vector<int>>& stones) {
        auto uf = UF{};
        for(auto stone: stones) {
            int r = stone[0], c = stone[1];
            uf.uni(r, c + OFFSET);
        }
        int islands = 0;
        for(auto [u, p]: uf.p) {
            if(u == p) islands++;
        }
        return stones.size() - islands;
    }
};
