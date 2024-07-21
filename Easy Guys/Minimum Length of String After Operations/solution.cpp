class Solution {
public:
    int minimumLength(string s) {
        unordered_map<char, int> m;
        for(auto c: s) {
            m[c] += 1;
            if(m[c] == 3) {
                m[c] -= 2;
            } 
        }
        int result = 0;
        for(auto it: m) {
            result += it.second;
        }
        return result;
    }
};
