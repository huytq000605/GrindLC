class Solution {
public:
    int numberOfWays(string corridor) {
        int MOD = 1e9 + 7;
        int result = 1;
        int seats = 0;
        int ways = 1;
        for(char c: corridor) {
            if(c == 'S') {
                if(seats == 2) {
                    result = (1LL * result * ways) % MOD;
                    ways = 1;
                    seats = 0;
                }
                ++seats;
            } else if(seats == 2) ++ways;
        }
        if(seats != 2) return 0;
        return result;
    }
};
