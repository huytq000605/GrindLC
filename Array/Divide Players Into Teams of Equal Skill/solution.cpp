class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int mn = skill[0], mx = skill[0];
        unordered_map<long long, long long> counter;
        for(int v: skill) {
            mn = min(mn, v);
            mx = max(mx, v);
            ++counter[v];
        }
        long long target = mn + mx;
        long long result = 0;
        for(auto & [v1, f1]: counter) {
            if(!f1) continue;
            long long v2 = target - v1;
            if(v1 == v2) {
                if(f1 % 2) return -1;
                result += v1 * v2 * f1 / 2;
            } else {
                long long & f2 = counter[v2];
                if(f1 != f2) return -1;
                result += v1 * v2 * f1;
                f2 = 0;
            }
            f1 = 0;
        }
        return result;

    }
};
