class UF {
vector<int> p;
vector<int> r;
vector<int> c;
public:
    UF(int n) {
        p = vector(n, 0);
        for(int i = 0; i < n; i++) p[i] = i;
        r = vector(n, 1);
        c = vector(n, (1<<18) - 1);
    }
    
    int find(int u) {
        if(u != p[u]) {
            p[u] = find(p[u]);
        }
        return p[u];
    }
    
    void unionf(int u, int v, int cost) {
        u = find(u), v = find(v);
        c[u] = c[u] & c[v] & cost;
        if(u != v) {
            p[v] = u;
            r[u] += r[v];
        }
    }
    
    int get_cost(int u, int v) {
        u = find(u), v = find(v);
        if(u != v) return -1;
        return c[u];
    }
};

class Solution {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        UF uf(n);
        for(auto & edge: edges) {
            int u = edge[0], v = edge[1], c = edge[2];
            uf.unionf(u, v, c);
        }
        vector<int> result;
        for(auto & q: query) {
            int a = q[0], b = q[1];
            result.push_back(uf.get_cost(a, b));
        }
        return result;
    }
};
