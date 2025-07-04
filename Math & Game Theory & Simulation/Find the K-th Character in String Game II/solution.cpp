class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        long long t = ceil(log(k)/log(2));
        long long n = 1ll << t;
        long long shift = 0;
        --k;
        int i = t - 1;
        while(n > 1) {
            n >>= 1;
            if(k >= n) {
                k -= n;
                shift = (shift + operations[i]) % 26;
            }
            --i;
        }
        return 'a' + (shift % 26);
    }
};
