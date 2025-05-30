class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n = edges.size();
        auto traversal = [&](int u) {
            vector<int> result(n, -1);
            result[u] = 0;
            int s = 0;
            while(true) {
                int v = edges[u];
                if(v == -1 || result[v] != -1) break;
                result[v] = ++s;
                u = v;
            }
            return result;
        };
        auto s1 = traversal(node1);
        auto s2 = traversal(node2);
        int mn_distance = INT_MAX;
        int result = -1;
        for(int i = 0; i < n; ++i) {
            if(s1[i] == -1 || s2[i] == -1) continue;
            int s = max(s1[i], s2[i]);
            if(s < mn_distance) {
                mn_distance = s;
                result = i;
            } 
        }
        return result;
    }
};
