class Solution {
public:
    int nonSpecialCount(int l, int r) {
        int sq = int(sqrt(r));
        vector<bool> is_prime(sq + 1, true);
        int special = 0;
        for(int i = 2; i <= sq; i++) {
            if(is_prime[i]) {
                if(i * i >= l && i * i <= r) special++;
                int num = i + i;
                while(num <= sq) {
                    is_prime[num] = false;
                    num += i;
                }
            }
        }
        return r - l + 1 - special;
    }
};
