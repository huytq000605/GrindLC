class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<long long> pq;
        for(int g: gifts) {
            pq.emplace(g);
        }
        while(k--) {
            int g = pq.top();
            pq.pop();
            g = static_cast<long long>(sqrt(static_cast<double>(g)));
            pq.emplace(g);
        }
        long long result{};
        while(!pq.empty()) {
            result += pq.top();
            pq.pop();
        }
        return result;
    }
};
