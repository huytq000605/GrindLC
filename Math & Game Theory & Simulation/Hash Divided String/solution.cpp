class Solution {
public:
    string stringHash(string s, int k) {
        string result;
        int m = s.size() / k;
        for(int i = 0; i < m; i++) {
            int sum = 0;
            for(int j = k * i; j < k*i + k; j++) {
                sum += s[j] - 'a';
            }
            result += (sum % 26) + 'a';
        }
        return result;
    }
};
