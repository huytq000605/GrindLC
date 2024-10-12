class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> callees(n, vector<int>());
        for(auto &edge: invocations) {
            int caller = edge[0], callee = edge[1];
            callees[caller].emplace_back(callee);
        }
        set<int> s;
        s.emplace(k);
        deque<int> dq;
        dq.emplace_back(k);
        while(!dq.empty()) {
            int u = dq.back();
            dq.pop_back();
            for(auto v: callees[u]) {
                if(s.find(v) != s.end()) continue;
                s.emplace(v);
                dq.emplace_front(v);
            }
        }
        vector<int> result;
        
        for(auto &edge: invocations) {
            int caller = edge[0], callee = edge[1];
            if(s.find(caller) != s.end()) continue;
            if(s.find(callee) != s.end()) {
                for(int i = 0; i < n; ++i) result.emplace_back(i);
                return result;
            }
        }
        
        for(int i = 0; i < n; ++i) if(s.find(i) == s.end()) result.emplace_back(i);
        return result;
    }
};
