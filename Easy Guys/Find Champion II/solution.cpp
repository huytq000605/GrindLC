class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<int> indegree(n);
        for(auto &edge: edges) {
            int u = edge[0], v = edge[1];
            ++indegree[v];
        }
        int champion{-1};
        for(int u{}; u < n; ++u) {
            if(indegree[u]) continue;
            if(champion != -1) return -1;
            champion = u;
        }
        return champion;
    }
};
