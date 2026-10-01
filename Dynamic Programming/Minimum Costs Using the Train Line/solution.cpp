class Solution {
public:
    vector<long long> minimumCosts(vector<int>& regular, vector<int>& express, int expressCost) {
        long long r = 0, e = expressCost;
        int n = regular.size();
        vector<long long> result(n);
        for(int i = 0; i < n; ++i) {
            long long nr = min(e + express[i], r + regular[i]);
            long long ne = min(e + express[i], r + regular[i] + expressCost);
            result[i] = min(nr, ne);
            r = nr;
            e = ne;
        }
        return result;
    }
};
