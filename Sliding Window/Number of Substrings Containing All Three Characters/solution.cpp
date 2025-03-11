class Solution {
public:
    int numberOfSubstrings(string s) {
        vector<int> counter(3);
        int result = 0;
        for(int i = 0, j = 0; i < s.size(); ++i) {
            counter[s[i] - 'a']++;
            while(counter[0] && counter[1] && counter[2]) {
                counter[s[j] - 'a']--;
                ++j;
            }
            result += j;
        }
        return result;
    }
};
