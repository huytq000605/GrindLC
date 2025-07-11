class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        priority_queue<int, vector<int>, decltype([](int r1, int r2) -> bool {
            return r1 > r2;
        })> free;
        priority_queue<pair<int, long long>, vector<pair<int, long long>>, decltype([](auto &p1, auto &p2) -> bool {
            if(p1.second == p2.second) {
                return p1.first > p2.first;
            }
            return p1.second > p2.second;
        })> used;
        vector<int> freq(n);
        for(int i = 0; i < n; ++i) free.emplace(i);
        int t = meetings.front()[0];
        for(auto &m: meetings) {
            int s = m[0], e = m[1];
            while(!used.empty() && used.top().second <= s) {
                free.emplace(used.top().first);
                used.pop();
            }
            if(!free.empty()) {
                int room = free.top(); free.pop();
                used.emplace(room, e);
                freq[room]++;
            } else {
                auto [room, t] = used.top(); used.pop();
                used.emplace(room, t+e-s);
                freq[room]++;
            }
        }
        int result = 0;
        for(int i = 1; i < n; ++i) {
            if(freq[i] > freq[result]) result = i;
        }
        return result;

    }
};
