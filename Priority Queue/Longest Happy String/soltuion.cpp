class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        string result{};
        priority_queue<pair<int, char>, vector<pair<int, char>>, 
            decltype([](auto &p1, auto &p2) -> bool {
                return p1.first < p2.first;
            })> pq{};
        if(a) pq.emplace(a, 'a');
        if(b) pq.emplace(b, 'b');
        if(c) pq.emplace(c, 'c');
        while(!pq.empty()) {
            auto [f, c] = pq.top();
            pq.pop();
            if(result.size() >= 2 && result[result.size() - 2] == result.back() && result.back() == c) {
                if(pq.empty()) break;
                auto [f2, c2] = pq.top();
                pq.pop();
                result += c2;
                if(f2-1) pq.emplace(f2-1, c2);
                pq.emplace(f, c);
            } else {
                result += c;
                if(f-1) pq.emplace(f-1, c);
            }
        }
        return result;
    }
};
