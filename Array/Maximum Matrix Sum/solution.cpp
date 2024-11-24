class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        int negative{};
        int zero{};
        int mn{INT_MAX};
        long long result{};
        for(auto &row: matrix) {
            for(auto v: row) {
                int av = abs(v);
                if(v < 0) negative ^= 1; 
                else if(v == 0) zero |= 1;
                mn = min(mn, av);
                result += av;
            }
        }
        if(!zero && negative) result -= 2 * mn;
        return result;
    }
};
