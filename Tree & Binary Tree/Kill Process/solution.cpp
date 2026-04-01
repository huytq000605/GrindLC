class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, int kill) {
        int n = pid.size();
        unordered_map<int, vector<int>> children;
        for(int i = 0; i < n; ++i) {
            if(!ppid[i]) continue;
            children[ppid[i]].push_back(pid[i]);
        }
        vector<int> q{kill};
        vector<int> result;
        while(!q.empty()) {
            int id = q.back();
            q.pop_back();
            result.push_back(id);
            for(int v: children[id]) q.push_back(v);
        }
        return result;
    }
};
