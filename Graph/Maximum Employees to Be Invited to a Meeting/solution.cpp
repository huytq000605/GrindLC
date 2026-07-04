class Solution {
public:
    int maximumInvitations(vector<int>& favorite) {
        int n = favorite.size();
        vector<int> indeg(n);
        for(int f: favorite) indeg[f]++;
        deque<int> dq;
        for(int u{}; u < n; ++u) {
            if(indeg[u] == 0) {
                dq.emplace_back(u);
            }
        }

        vector<int> chain_length(n);
        vector<bool> visited(n);
        while(!dq.empty()) {
            auto u = dq.front(); dq.pop_front();
            visited[u] = true;
            int v = favorite[u];
            chain_length[v] = max(chain_length[v], chain_length[u] + 1);
            indeg[v] -= 1;
            if(!indeg[v]) dq.emplace_back(v);
        }

        int max_cycle{};
        int total_chains{};
        for(int u{}; u < n; ++u) {
            if(visited[u]) continue; // this person is belong to a chain
            // this person does not belong to a chain, so it must be in a cycle
            int v = u;
            int cycle_length{};
            while(!visited[v]) {
                visited[v] = true;
                v = favorite[v];
                cycle_length++;
            }
            
            // special case for cycle length 2, it contributes directly to the chain
            if(cycle_length == 2) {
                total_chains += 2 + chain_length[u] + chain_length[favorite[u]];
            } else {
                max_cycle = max(max_cycle, cycle_length);
            }
            
        }

        return max(max_cycle, total_chains);
    }
};
