class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> deadends_set(deadends.begin(), deadends.end());
        if(deadends_set.contains("0000")) return -1;
        deque<pair<string, int>> dq;
        dq.emplace_back("0000", 0);
        unordered_set<string> seen;
        seen.emplace("0000");
        while(dq.size()) {
            auto p = dq.front();
            dq.pop_front();
            auto cur = p.first;
            auto steps = p.second;
            if(cur == target) return steps;
            for(int i = 0; i < 4; i++) {
                char forward = ((cur[i] - '0') + 1 + 10) % 10 + '0';
                char backward = ((cur[i] - '0') - 1 + 10) % 10 + '0';
                for(auto & chr : vector<char>{forward, backward}) {
                    string nxt = (i > 0 ? cur.substr(0, i) : "") + string(1, chr) + (i + 1 < 4 ? cur.substr(i+1, 4) : "");
                    if(!seen.contains(nxt) && !deadends_set.contains(nxt)) {
                        seen.emplace(nxt);
                        dq.emplace_back(nxt, steps + 1);
                    }
                }
            }
        }
        return -1;
    }
};
