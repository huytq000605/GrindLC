class UF {
int n;
vector<int> p;
vector<int> r;
public:
    UF(int m) {
        n = m;
        p = vector<int>(n, 0);
        for(int i = 0; i < n; i++) {
            p[i] = i;
        }
        r = vector<int>(n, 1);
    }

    int find(int u) {
        if(p[u] != u) {
            p[u] = find(p[u]);
        }
        return p[u];
    }

    int uni(int u, int v) {
        u = find(u), v = find(v);
        if(u == v) return 0;
        if(r[u] < r[v]) swap(u, v);
        p[v] = u;
        r[u] += r[v];
        return 1;
    }
};

class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        int mn = m * n;
        UF uf = UF(mn);
        pair<int, int> ds[4] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        set<pair<int, int>> islands;
        int island_count = 0;
        vector<int> result;
        for(auto & p: positions) {
            int r = p[0], c = p[1];
            if(islands.contains({r, c})) {
                result.push_back(island_count);
                continue;
            }
            island_count += 1;
            islands.emplace(r, c);
            for(auto & d: ds) {
                int dr = d.first, dc = d.second;
                int ar = r + dr, ac = c + dc;
                if(ar < 0 || ar >= m || ac < 0 || ac >= n) continue;
                if(!islands.contains({ar, ac})) continue;
                island_count -= uf.uni(r * n + c, ar * n + ac);
            }
            result.push_back(island_count);
        }
        return result;
        
    }
};
