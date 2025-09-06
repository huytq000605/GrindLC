class Solution {
public:
    long long minOperations(vector<vector<int>>& queries) {
        long long result = 0;
        vector<long long> pow4;
        pow4.push_back(1);
        for(int i = 0; i < 15; ++i) {
            pow4.push_back(pow4.back() * 4);
        }
        for(auto &q: queries) {
            int s = floor(log(q[0]) / log(4));
            int e = floor(log(q[1]) / log(4));
            int upper = q[1];
            long long res = 0;
            for(int i = e; i >= s; --i) {
                int lower = i == s ? q[0]: pow4[i];
                int t = i + 1;
                int n = upper-lower+1;
                res += 1LL * n * t;
                upper = lower-1;
            }
            result += (res + 1) / 2;
        }
        return result;
    }
};
