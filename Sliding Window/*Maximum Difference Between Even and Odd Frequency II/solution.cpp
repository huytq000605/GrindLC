class Solution {
public:
    int maxDifference(string s, int k) {
        int result{INT_MIN};
        for(char a = '0'; a <= '4'; ++a) {
            for(char b = '0'; b <= '4'; ++b) {
                if(a == b) continue;
                deque<pair<int, int>> counter;
                map<pair<int, int>, int> m;
                counter.emplace_back(0, 0);
                for(int i = 0; i < s.size(); ++i) {
                    counter.emplace_back(counter.back());
                    if(s[i] == a) counter.back().first++;
                    else if(s[i] == b) counter.back().second++;
                    while(counter.size() > k && // we have at least k elements
                         // make sure we have at least one a and b
                          counter.front().first < counter.back().first && 
                          counter.front().second < counter.back().second) {
                        auto [ca, cb] = counter.front(); counter.pop_front();
                        auto key = make_pair(ca%2, cb%2);
                        m[key] = m.find(key) == m.end() ? ca-cb: min(m[key], ca-cb);
                    }
                    auto [ca, cb] = counter.back();
                    int diff = ca - cb;
                    auto seen_key = make_pair(1 - (ca%2), cb % 2);
                    if(m.find(seen_key) != m.end()) {
                        result = max(result, diff - m[seen_key]);
                    }

                }
            }
        }
        return result;
    }
};
