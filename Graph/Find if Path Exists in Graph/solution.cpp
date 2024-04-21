class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> graph(n, vector<int>());
        for(auto & e: edges) {
            int u = e[0], v = e[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        stack<int> st;
        st.push(source);
        while(st.size()) {
            int u = st.top();
            if(u == destination) return true;
            st.pop();
            for(auto & v: graph[u]) {
                st.push(v);
            }
            graph[u].resize(0);
        }
        return false;
    }
};
