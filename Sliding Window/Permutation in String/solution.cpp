class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::array<int, 26> counter;
        for(char c: s1) ++counter[c - 'a'];
        for(int i = 0; i < s2.size(); ++i) {
            if(i >= s1.size()) ++counter[s2[i - s1.size()] - 'a'];
            --counter[s2[i] - 'a'];
            bool valid = true;
            for(int c: counter)
                if(c > 0) {
                    valid = false;
                    break;
                }
            if(valid) return true;
        }
        return false;
    }
};
