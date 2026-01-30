class Solution {
public:
    long long minimumCost(string source, string target, vector<string>& original, vector<string>& changed, vector<int>& cost) {
        unordered_map<string, unordered_map<string, int>> graph;
        unordered_set<int> lengths;
        for(int i = 0; i < original.size(); ++i) {
            auto &um = graph[original[i]];
            if(um.find(changed[i]) == um.end() || cost[i] < um[changed[i]])
                graph[original[i]][changed[i]] = cost[i];
            lengths.emplace(original[i].size());
        }
        auto dijkstra = [&](string& start) -> unordered_map<string, long long> {
            unordered_map<string, long long> result;
            priority_queue<pair<string, long long>, vector<pair<string, long long>>, decltype([](auto &p1, auto &p2) -> bool {
                return p1.second > p2.second;
            })> pq;
            pq.emplace(start, 0ll);
            while(!pq.empty()) {
                auto [str, s] = pq.top(); pq.pop();
                for(auto &[nstr, ds]: graph[str]) {
                    if(result.find(nstr) == result.end() || s + ds < result[nstr]) {
                        result[nstr] = s + ds;
                        pq.emplace(nstr, s + ds);
                    }
                }
            }
            return result;
        };
        unordered_map<string, unordered_map<string, long long>> costs;
        for(auto& s: original) {
            costs[s] = dijkstra(s);
        }
        vector<long long> dp(source.size() + 1, LLONG_MAX);
        dp[0] = 0;
        for(int i = 0; i < source.size(); ++i) {
            if(source[i] == target[i]) {
                dp[i+1] = min(dp[i+1], dp[i]);
            }
            for(int length: lengths) {
                if(i+1-length < 0) continue; 
                if(dp[i+1-length] == LLONG_MAX) continue;
                string s = source.substr(i-length+1, length);
                string t = target.substr(i-length+1, length);
                if(s == t) {
                    dp[i+1] = min(dp[i+1], dp[i+1-length]);
                } else if(costs.find(s) != costs.end() && costs[s].find(t) != costs[s].end()) {
                    dp[i+1] = min(dp[i+1], dp[i+1-length] + costs[s][t]);
                }
            }
        }
        return dp.back() == LLONG_MAX ? -1: dp.back();
    }
};
