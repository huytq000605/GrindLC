class Solution {
public:
    long long minDamage(int power, vector<int>& damage, vector<int>& health) {
        int n = damage.size();
        // damage, time
        vector<pair<int, int>> enemies(n);
        for(int i = 0; i < n; ++i) enemies[i] = make_pair(damage[i], ceil(static_cast<double>(health[i]) / power));
        // kill e1, cost is d1t1 + d2t1 + d2t2
        // kill e2, cost is d2t2 + d1t1 + d1t2
        // => diff is d2t1 and d1t2 ~ d1/t1 and d2/t2
        // => sort by d/t
        sort(enemies.begin(), enemies.end(), [](auto e1, auto e2) {
            return static_cast<double>(e1.first) / e1.second > static_cast<double>(e2.first) / e2.second;  
        });
        long long result = 0;
        int t = 0;
        for(auto e: enemies) {
            t += e.second;
            result += static_cast<long long>(e.first) * t;
        }
        return result;
    }
};
