class Solution {
public:
    vector<bool> checkIfPrerequisite(int n, vector<vector<int>>& prereqs, vector<vector<int>>& queries) {
        vector<unordered_set<int>> reqs(n);
        for(auto &prereq: prereqs) {
            int u = prereq[0], v = prereq[1];
            reqs[v].emplace(u);
        }

        vector<vector<int>> memo(n, vector<int>(n, -1));
        function<bool(int, int)> is_req = [&](int u, int v) -> bool {
            if(memo[u][v] != -1) return static_cast<bool>(memo[u][v]);
            if(reqs[v].find(u) != reqs[v].end()) return true;
            for(auto w: reqs[v]) {
                if(is_req(u, w)) {
                    memo[u][v] = 1;
                    return true;
                }
            }

            memo[u][v] = 0;
            return false;
        };

        vector<bool> result;
        for(auto &query: queries) {
            int u = query[0], v = query[1];
            result.emplace_back(is_req(u, v));
        }
        return result;
    }
};
