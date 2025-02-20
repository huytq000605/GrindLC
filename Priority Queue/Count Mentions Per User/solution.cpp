class Solution {
public:
    vector<int> countMentions(int n, vector<vector<string>>& events) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        sort(events.begin(), events.end(), [](auto &e1, auto &e2) {
            int t1 = stoi(e1[1]), t2 = stoi(e2[1]);
            if(t1 == t2) {
                return e1[0] == "OFFLINE";
            }
            return t1 < t2;
        });
        
        vector<int> offline(n);
        vector<int> result(n);
        for(auto &event: events) {
            if(event[0] == "MESSAGE") {
                while(!pq.empty() && stoi(event[1]) >= pq.top().first) {
                    offline[pq.top().second] -= 1;
                    pq.pop();
                }
                if(event[2] == "ALL") {
                    for(int i{}; i < n; ++i) result[i]++;
                } else if(event[2] == "HERE") {
                    for(int i{}; i < n; ++i) if(!offline[i]) result[i]++;
                } else {
                    int id{-1};
                    string& s{event[2]};
                    for(int i{2}; i < s.size(); ++i) {
                        if(s[i] == ' ') {
                            result[id]++;
                            i += 2;
                            id = -1;
                            continue;
                        } else {
                            if(id == -1) id = 0;
                            id = id * 10 + (s[i] - '0');
                        }
                    }
                    result[id]++;
                }
            } else {
                offline[stoi(event[2])]++;
                pq.emplace(stoi(event[1]) + 60, stoi(event[2]));
            }
        }
        
        return result;
    }
};
