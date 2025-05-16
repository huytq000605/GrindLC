class Solution {
    bool valid(string& s1, string& s2) {
        if(s1.size() != s2.size()) return false;
        for(int i = 0, diff = 0; i < s1.size(); ++i) {
            diff += s1[i] != s2[i];
            if(diff > 1) return false;
        }
        return true;
    }
public:
    vector<string> getWordsInLongestSubsequence(vector<string>& words, vector<int>& groups) {
        int n = words.size();
        vector<int> dp(n, 1);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < i; ++j) {
                if(valid(words[i], words[j]) && groups[i] != groups[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        vector<string> result;
        int target = *max_element(dp.begin(), dp.end());
        cout << target << endl;
        for(int i = n-1, j = n; i >= 0; --i) {
            if(dp[i] == target && (j == n || (valid(words[i], words[j]) && groups[i] != groups[j]))) {
                result.emplace_back(words[i]);
                j = i;
                --target;
                if(!target) break;
            }
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
