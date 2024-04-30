class Solution {
public:
    long long wonderfulSubstrings(string word) {
        int bits[1024] = {0};
        bits[0] = 1;
        int mask = 0;
        long long result = 0;
        for(char & c : word) {
            mask ^= 1 << (c - 'a');
            for(int bit = 0; bit < 10; bit++) {
                result += bits[mask ^ (1 << bit)];
            }
            result += bits[mask ^ 0];
            bits[mask] += 1;
        }
        return result;
    }
};
