class Solution {
public:
    vector<int> countMentions(int n, vector<vector<string>>& events) {
        sort(events.begin(), events.end(), [](auto &e1, auto &e2) {
            int t1 = stoi(e1[1]), t2 = stoi(e2[1]);
            if(t1 == t2) return e1[0] == "OFFLINE";
            return t1< t2;
        });
        deque<pair<int, int>> dq;
        vector<int> online(n, 1);
        vector<int> result(n);
        int all = 0;
        for(auto &e: events) {
            int t = stoi(e[1]);
            while(!dq.empty() && dq.front().first <= t) {
                auto [t, u] = dq.front();
                online[u] = 1;
                dq.pop_front();
            }
            if(e[0] == "MESSAGE") {
                if(e[2] == "ALL") {
                    ++all;
                } else if(e[2] == "HERE") {
                    for(int u = 0; u < n; ++u) if(online[u]) result[u]++;
                } else {
                    int id = 0;
                    for(char c: e[2]) {
                        if(c == 'i' || c == 'd') {
                            continue;
                        } else if(c == ' ') {
                            result[id]++;
                            id = 0;
                        }
                        else id = id * 10 + (c - '0');
                    }
                    result[id]++;
                }
            } else {
                online[stoi(e[2])] = 0;
                dq.emplace_back(stoi(e[1]) +  60, stoi(e[2]));
            }
        }
        for(int u = 0; u < n; ++u) result[u] += all;
        return result;
    }
};
