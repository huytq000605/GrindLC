class Solution {
    vector<int> kmp(string& s, string& p) {
        int ss = s.size(), ps = p.size();
        vector<int> lpsp(ps), lpss(ss);
        for(int i = 1, j = 0; i < ps; ++i) {
            while(j && p[i] != p[j]) {
                j = lpsp[j-1];
            }
            if(p[i] == p[j]) {
                ++j;
                lpsp[i] = j;
            }
        }
        for(int i = 0, j = 0; i < ss; ++i) {
            while(j && s[i] != p[j]) {
                j = lpsp[j-1];
            }
            if(s[i] == p[j]) ++j;
            lpss[i] = j;
            if(j == ps) {
                j = lpsp[j-1];
            }
        }
        return lpss;
    }
public:
    int shortestMatchingSubstring(string s, string p) {
        if(p.size() == 2) return 0;
        vector<string> patterns;
        for(int i{}, j{}; i < p.size(); ++i) {
            if(p[i] == '*') {
                if(i - j > 0) patterns.emplace_back(p.substr(j, i - j));
                j = i+1;
            } else if(i == p.size() - 1) {
                if(i - j + 1 > 0) patterns.emplace_back(p.substr(j, i - j + 1));
            }
        }

        vector<vector<int>> kmps(patterns.size());
        for(int p = 0; p < patterns.size(); ++p) {
            kmps[p] = kmp(s, patterns[p]);
        }
        vector<int> idxs(patterns.size(), 0);
        int n = s.size();
        int result = n+1;
        while(*max_element(idxs.begin(), idxs.end()) < n) {
            for(int p = 0; p < patterns.size(); ++p) {
                if(p) {
                    int ps = patterns[p].size();
                    idxs[p] = max(idxs[p], idxs[p-1] + ps);
                }
                
                if(!patterns[p].empty()) {
                    while(idxs[p] < n && kmps[p][idxs[p]] < patterns[p].size()) {
                        ++idxs[p];
                    }
                }
            }

            if(*max_element(idxs.begin(), idxs.end()) < n) {
                int start = idxs[0] + 1 - static_cast<int>(patterns[0].size());
                result = min(result, idxs.back() - start + 1);
            }
            ++idxs[0];
        }
        if(result == n+1) return -1;
        return result;
    }
};
