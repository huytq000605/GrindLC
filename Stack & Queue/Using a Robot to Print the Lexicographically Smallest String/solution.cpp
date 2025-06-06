class Solution {
public:
    string robotWithString(string s) {
        vector<int> counter(26);
        for(char c: s) {
            counter[c-'a']++;
        }
        vector<char> st;
        string result;
        for(int i = 0, target = 0; i < s.size();) {
            while(!counter[target]) ++target;
            char c = target + 'a';

            while(!st.empty() && st.back() <= c) {
                result += st.back(); st.pop_back();
            }

            while(i < s.size() && s[i] != c) {
                st.emplace_back(s[i]);
                counter[s[i] - 'a']--;
                ++i;
            }
            counter[target]--;
            result += c;
            ++i;
        }
        while(!st.empty()) {
            result += st.back(); st.pop_back();
        }
        return result;
    }
};
