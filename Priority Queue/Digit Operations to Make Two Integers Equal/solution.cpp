static inline vector<int> IS_PRIME(1e5+1, 1);

class Solution {
public:
    int minOperations(int n, int m) {
        if(IS_PRIME[0]) {
            IS_PRIME[0] = IS_PRIME[1] = 0;
            for(int i{2}; i <= 1e5; ++i) {
                if(!IS_PRIME[i]) continue;
                for(int num{i+i}; num <= 1e5; num += i) {
                    IS_PRIME[num] = 0;
                }
            }
        }
        if(IS_PRIME[n] || IS_PRIME[m]) return -1;
        int digits = to_string(n).size();
        priority_queue<pair<int, int>, vector<pair<int, int>>,
            decltype([](auto p1, auto p2) -> bool {
                return p1.first > p2.first;
            })> pq;
        pq.emplace(n, n);
        unordered_set<int> visited;
        visited.emplace(n);
        while(!pq.empty()) {
            auto [s, num] = pq.top();
            if(num == m) return s;
            for(int d{}; d < digits; ++d) {
                int power = static_cast<int>(pow(10, d));
                int digit = (num / power) % 10;
                if(digit != 9) {
                    int next_num = num + power;
                    if(!IS_PRIME[next_num] && visited.find(next_num) == visited.end()) {
                        visited.emplace(next_num);
                        pq.emplace(s + num + power, next_num);
                    }
                    
                }
                if(digit != 0 && !(d == digits - 1 && digit == 1)) {
                    int next_num = num - power;
                    if(!IS_PRIME[next_num] && visited.find(next_num) == visited.end()) {
                        visited.emplace(next_num);
                        pq.emplace(s + num - power, next_num);
                    }
                }
            }
            pq.pop();
        }
        return -1;
    }
};
