class Solution {
public:
    string rearrangeString(string s, int k) {
        vector<int> counter(26);
        for(char c: s) counter[c-'a']++;
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype([](auto &p1, auto &p2) -> bool {
            return p1.first < p2.first;
        })> pq;
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, decltype([](auto &t1, auto &t2) -> bool {
            return get<0>(t1) > get<0>(t2);
        })> pending;
        for(int i = 0; i < 26; ++i) {
            if(!counter[i]) continue;
            pq.emplace(counter[i], i);
        }
        string result;
        for(int i = 0; !pq.empty() || !pending.empty(); ++i) {
            while(!pending.empty() && i >= get<0>(pending.top())) {
                auto [_, f, c] = pending.top(); pending.pop();
                pq.emplace(f, c);
            }
            if(pq.empty()) return "";
            auto [f, c] = pq.top(); pq.pop();
            result += (c + 'a');
            --f;
            if(f) {
                pending.emplace(i + k, f, c);
            }
        }
        return result;
    }
};
