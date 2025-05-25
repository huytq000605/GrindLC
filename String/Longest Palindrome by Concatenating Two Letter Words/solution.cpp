class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> m;
        int result = 0;
        int unpaired = 0;
        for(auto &w: words) {
            if(w[0] == w[1]) {
                if(m.find(w) != m.end() && m[w]) {
                    result += 4;
                    --unpaired;
                    --m[w];
                } else {
                    ++unpaired;
                    ++m[w];
                }
            } else {
                string r = w;
                reverse(r.begin(), r.end());
                if(m.find(r) != m.end() && m[r]) {
                    --m[r];
                    result += 4;
                } else {
                    ++m[w];
                }
            }
        }
        return result + (unpaired ? 2: 0);
    }
};
