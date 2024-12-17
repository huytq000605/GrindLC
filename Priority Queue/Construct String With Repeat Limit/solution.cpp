class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        vector<int> counter(26, 0);
        for(char c: s) ++counter[c - 'a'];
        priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> pq;
        for(int c{}; c < 26; ++c) if(counter[c]) pq.emplace(c, counter[c]);
        string result{};
        int repeat{};
        while(!pq.empty()) {
            auto [c, f] = pq.top();
            pq.pop();
            if(!result.empty() && result.back() == c + 'a') {
                if(pq.empty()) return result;
                auto [c2, f2] = pq.top();
                pq.pop();
                result += (c2 + 'a');
                repeat = 1;
                if(f2-1) pq.emplace(c2, f2-1);
                pq.emplace(c, f);
            } else {
                int k = min(repeatLimit, f);
                f -= k;
                if(f) pq.emplace(c, f);
                result += string(k, c + 'a');
            }
        }
        return result;
    }
};
