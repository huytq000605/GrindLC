class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        map<int, int> m;
        for(int f: basket1) m[f] += 1;
        for(int f: basket2) m[f] -= 1;
        int mn = m.begin()->first;
        long long result = 0;
        vector<int> swaps;
        for(auto [f, freq]: m) {
            if(freq & 1) return -1;
            for(int i = 0; i < abs(freq) / 2; ++i) swaps.push_back(f);
        }
        for(int i = 0; i < swaps.size() / 2; ++i) result += min(mn*2, swaps[i]);
        return result;
    }
};
