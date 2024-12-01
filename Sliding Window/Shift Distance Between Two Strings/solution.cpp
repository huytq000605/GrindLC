class Solution {
public:
    long long shiftDistance(string s, string t, vector<int>& nextCost, vector<int>& previousCost) {
        vector<long long> prefix_next(26, 0);
        vector<long long> prefix_prev(26, 0);
        for(int i{}; i < 26; ++i) {
            if(i) {
                prefix_next[i] = prefix_next[i-1];
                prefix_prev[i] = prefix_prev[i-1];
            }
            prefix_next[i] += nextCost[i];
            prefix_prev[i] += previousCost[i];
        }
        long long result{};
        for(int i{}; i < s.size(); ++i) {
            long long cost{};
            if(s[i] < t[i]) {
                cost = prefix_next[t[i] - 'a' - 1] - (s[i] - 'a' > 0 ? prefix_next[s[i] - 'a' - 1] : 0);
                cost = min(cost, prefix_prev[s[i] - 'a'] + prefix_prev.back() - prefix_prev[t[i] - 'a']);
            } else if(s[i] > t[i]) {
                cost = prefix_prev[s[i] - 'a'] - prefix_prev[t[i] - 'a'];
                cost = min(cost, prefix_next.back() - prefix_next[s[i] - 'a' - 1] + (t[i] - 'a' > 0 ? prefix_next[t[i] - 'a' - 1] : 0));
            }
            result += cost;
        }
        return result;
        
    }
};
