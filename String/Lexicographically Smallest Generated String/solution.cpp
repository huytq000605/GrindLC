class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.size(), m = str2.size();
        string result(m+n-1, 'a');
        vector<bool> fixed(m+n-1, false);
        for(int i{}; i < n; ++i) {
            if(str1[i] == 'T') {
                for(int j = 0; j < m; ++j) {
                    if(fixed[i+j] && result[i+j] != str2[j]) return "";
                    result[i+j] = str2[j];
                    fixed[i+j] = true;
                }
            }
        }
        for(int i{}; i < n; ++i) {
            if(str1[i] == 'F') {
                int diff = 0;
                for(int j = 0; j < m; ++j) {
                    if(result[i+j] != str2[j]) ++diff;
                }
                bool valid = true;
                if(!diff) {
                    valid = false;
                    for(int j = m-1; j >= 0; --j) {
                        if(!fixed[i+j]) {
                            result[i+j] = str2[j] == 'a' ? 'b': 'a';
                            valid = true;
                            break;
                        }
                    }
                }
                if(!valid) return "";
            }
        }
        return result;
    }
};
