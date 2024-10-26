class Solution {
public:
    int numberOfSubstrings(string s, int k) {
        vector<int> counter(26, 0);
        auto valid = [&]() -> bool {
            for(int c: counter) if(c >= k) return true;
            return false;
        };
        int result = 0;
        int j = 0;
        for(int i = 0; i < s.size(); ++i) {
            ++counter[s[i] - 'a'];
            while(valid()) {
                --counter[s[j] - 'a'];
                ++j;
            }
            result += j;
        }
        return result;
    }
};
