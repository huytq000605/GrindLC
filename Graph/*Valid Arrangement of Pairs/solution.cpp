class Solution {
public:
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        unordered_map<int, vector<int>> graph;
        unordered_map<int, int> deg;
        for(auto &pair: pairs) {
            int u = pair[0], v = pair[1];
            graph[u].emplace_back(v);
            ++deg[u];
            --deg[v];
        }
        int u = pairs[0][0];
        for(auto [v, _]: deg) {
            if(deg[u] < deg[v]) u = v;
        }

        vector<int> vertices;
        stack<int> st;
        st.emplace(u);
        while(!st.empty()) {
            while(!graph[st.top()].empty()) {
                int u = st.top();
                st.emplace(graph[u].back());
                graph[u].pop_back();
            }
            vertices.emplace_back(st.top());
            st.pop();
        }
        reverse(vertices.begin(), vertices.end());

        vector<vector<int>> result(vertices.size() - 1);
        for(int i{}; i < vertices.size() - 1; ++i) {
            result[i] = {vertices[i], vertices[i+1]};
        }
        

        return result;
    }
};
