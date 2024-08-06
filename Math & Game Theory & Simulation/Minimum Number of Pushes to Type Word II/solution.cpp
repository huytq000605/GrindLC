class Solution {
public:
    int minimumPushes(string word) {
        vector<int> freqs(26, 0);
        for(auto c: word) freqs[c - 'a']++;
        sort(freqs.begin(), freqs.end(), greater<int>());
        int i = 0, result = 0;
        for(auto f: freqs) {
            if(!f) continue;
            result += f * (i++ / 8 + 1);
        }
        return result;
    }
};
