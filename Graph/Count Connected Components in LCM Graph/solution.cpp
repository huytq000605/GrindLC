class UF {
vector<int> p;
vector<int> r;
int n;
public:
    UF(int _n): n(_n) {
        p.resize(n);
        for(int i{}; i < n; ++i) p[i] = i;
        r.resize(n, 1);
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
        p[v] = u;
        r[u] += r[v];
    }
};

class Solution {
public:
    int countComponents(vector<int>& nums, int threshold) {
        UF uf{threshold+1};
        for(int num: nums) {
            if(num > threshold) continue;
            for(int k{2}; num * k <= threshold; ++k) {
                uf.uni(num, num*k);
            }
        }
        int result{};
        for(int num: nums) {
            if(num > threshold || uf.find(num) == num) ++result;
        }
        return result;
    }
};
