class Solution {
public:
    int minOperations(string s, int k) {
        int64_t z = count(begin(s), end(s), '0');
        int64_t n = s.size();
        int64_t o = n - z;
        if(!z) return 0;
        for(int64_t i = 1; i <= n; ++i) {
            int64_t p = i * k;
            if(p < z || (p-z) & 1) continue;
            if(i & 1) {
                if(p <= (i * z + (i-1) * o)) return i;
            } else if(p <= ((i-1) * z + i * o)) return i;
        }
        return -1;
    }
};
