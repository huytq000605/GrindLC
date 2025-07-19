class UF {
public:
    int n;
    vector<long long> p, r, s;
    UF(vector<vector<int>> &grid) {
        n = grid.size();
        p.resize(n*n);
        r.resize(n*n, 1);
        s.resize(n*n);
        for(int r{}; r < n; ++r) {
            for(int c{}; c < n; ++c) {
                s[r*n+c] = grid[r][c];
                p[r*n+c] = r*n+c;
            }
        }
    }

    int find(int u) {
        if(u != p[u]) {
            p[u] = find(p[u]);
        }
        return p[u];
    }

    void uni(int u, int v) {
        u = find(u);
        v = find(v);
        if(u == v) return;
        if(r[u] < r[v]) swap(u, v);
        r[u] += r[v];
        s[u] += s[v];
        p[v] = u;
    }
};

class Solution {
public:
    long long sumRemoteness(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<pair<int, int>> ds{{0,1}, {1,0}, {-1,0}, {0,-1}};
        long long s{};
        auto uf = UF(grid);
        for(int r{}; r < n; ++r) {
            for(int c{}; c < n ; ++c) {
                if(grid[r][c] != -1) {
                    s += grid[r][c];
                    for(auto [dr, dc]: ds) {
                        int nr = r + dr, nc = c + dc;
                        if(nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
                        if(grid[nr][nc] == -1) continue;
                        uf.uni(r*n+c, nr*n+nc);
                    }
                }
            }
        }
        long long result{};
        for(int r{}; r < n; ++r) {
            for(int c{}; c < n; ++c) {
                if(grid[r][c] != -1) {
                    result += s - uf.s[uf.find(r*n+c)];
                }
            }
        }
        return result;

    }
};
