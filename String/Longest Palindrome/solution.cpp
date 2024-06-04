class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> counter;
        int result = 0;
        int odd = 0;
        for(char c: s) {
            counter[c] += 1;
        }
        for(auto [_, v]: counter) {
            result += v & (~1);
            odd = max(odd, v%2);
        }
        return result + odd;
    }
};
