class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> counter(26);
        for (auto c: s) {
            counter[c - 'a'] += 1;
        }
        string result;
        for (auto c: order) {
            while(counter[c - 'a']) {
                counter[c - 'a'] -= 1;
                result += c;
            }
        }
        for(int i = 0; i < 26; i++) {
            while(counter[i]) {
                result += i + 'a';
                counter[i] -= 1;
            }
        }
        return result;
    }
};
