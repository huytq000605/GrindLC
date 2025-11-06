class Solution {
public:
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        vector<int> online(c, 1);
        vector<int> p(c);
        vector<int> r(c, 1);
        for(int i = 0; i < c; ++i) {
            p[i] = i;
        }
        auto find = [&](this auto&& find, int u) -> int {
            if(u != p[u]) {
                p[u] = find(p[u]);
            }
            return p[u];
        };
        auto uni = [&](int u, int v) {
            u = find(u);
            v = find(v);
            if(u == v) return;
            if(r[u] < r[v]) swap(u, v);
            r[u] += r[v];
            p[v] = u;
        };
        
        for(auto &con: connections) {
            uni(con[0]-1, con[1]-1);
        }
        vector<vector<int>> groups(c);
        for(int i = c-1; i >= 0; --i) {
            groups[find(i)].push_back(i);
        }
        vector<int> result;
        for(auto &q: queries) {
            q[1] -= 1;
            if(q[0] == 1) {
                if(online[q[1]]) {
                    result.push_back(q[1] + 1);
                } else {
                    int g = find(q[1]);
                    result.push_back(groups[g].empty() ? -1: groups[g].back() + 1);
                }
            } else {
                int g = find(q[1]);
                online[q[1]] = 0;
                while(!groups[g].empty() && !online[groups[g].back()]) {
                    groups[g].pop_back();
                }
            }
        }
        return result;
    }
};
