class Solution {
public:
using P = tuple<string, string, string>;
using V = tuple<string, int, string>;
    bool lt(P &p1, P &p2) {
        if(get<0>(p1) == get<0>(p2)) {
            if(get<1>(p1) == get<1>(p2)) {
                return get<2>(p1) < get<2>(p2);
            }
            return get<1>(p1) < get<1>(p2);
        }
        return get<0>(p1) < get<0>(p2);
    }

    vector<string> mostVisitedPattern(vector<string>& username, vector<int>& timestamp, vector<string>& website) {
        map<P, int> score;
        unordered_map<string, vector<string>> w_by_u;
        vector<V> vs;
        unordered_map<string, set<P>> seen;
        for(int i = 0; i < username.size(); ++i) {
            string& u = username[i];
            int t = timestamp[i];
            string& w = website[i];
            vs.emplace_back(u, t, w);
        }
        sort(vs.begin(), vs.end(), [](auto &t1, auto &t2) -> bool {
            return get<1>(t1) < get<1>(t2);
        });
        int max_score = 0;
        P result = {"", "", ""};
        for(auto &v: vs) {
            auto [u, t, w] = v;
            w_by_u[u].push_back(w);
            if(w_by_u[u].size() >= 3) {
                int n = w_by_u[u].size();
                for(int i = 0; i <= n-3; ++i) {
                    for(int j = i+1; j <= n-2; ++j) {
                        string& w1 = w_by_u[u][i];
                        string& w2 = w_by_u[u][j];
                        string& w3 = w_by_u[u][n-1];
                        P k = {w1, w2, w3};
                        if(seen[u].find(k) != seen[u].end()) continue;
                        seen[u].insert(k);
                        score[k]++;
                        if(score[k] > max_score) {
                            max_score = score[k];
                            result = k;
                        } else if(score[k] == max_score && lt(k, result)) {
                            result = k;
                        }
                    }
                }
            }
        }
        auto [w1, w2, w3] = result;
        return {w1, w2, w3};
    }
};
