class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        sort(begin(meetings), end(meetings), [](auto& m1, auto& m2) -> bool {
            return m1[2] < m2[2];
        });
        vector<int> p(n), r(n, 1);
        for(int i = 0; i < n; ++i) p[i] = i;
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
            p[v] = u;
            r[u] += r[v];
        };
        auto reset = [&](int u) {
            p[u] = u;
            r[u] = 1;
        };
        uni(0, firstPerson);
        for(int i = 0; i < meetings.size();) {
            int start = i;
            unordered_set<int> s;
            while(i < meetings.size() && meetings[start][2] == meetings[i][2]) {
                s.insert(meetings[i][0]);
                s.insert(meetings[i][1]);
                uni(meetings[i][0], meetings[i][1]);
                ++i;
            }
            for(int u: s) if(find(u) != find(0)) reset(u);
        }
        vector<int> result;
        for(int u = 0; u < n; ++u) {
            if(find(u) == find(0)) result.push_back(u);
        }
        return result;
    }
};
