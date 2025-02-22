class Solution {
public:
    int maxDifference(string s) {
        vector<int> counter(26);
        for(char c: s) counter[c - 'a']++;
        int max_odd{}, min_even{101};
        for(int c: counter) {
            if(!c) continue;
            if(c & 1) {
                max_odd = max(max_odd, c);
            } else {
                min_even = min(min_even, c);
            }
        }
        if(min_even == 101) min_even = 0;
        return max_odd - min_even;
    }
};
