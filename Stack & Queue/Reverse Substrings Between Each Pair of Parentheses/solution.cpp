class Solution {
public:
    string reverseParentheses(string s) {
        int n = s.size();
        vector<int> link(n, -1), st;
        for(int i = 0; i < n; ++i) {
            if(s[i] == '(') st.push_back(i);
            else if(s[i] == ')') {
                int j = st.back(); st.pop_back();
                link[i] = j;
                link[j] = i;
            }
        }
        string result;
        for(int i = 0, di = 1; i < n; i += di) {
            if(link[i] != -1) {
                i = link[i];
                di = -di;
            } else {
                result += s[i];
            }
        }
        return result;
    }
};
