class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string> result;
        for(char c: s) {
            if(result.empty() || result.back().size() == k) result.emplace_back();
            result.back() += c;
        }
        result.back() += string(k - result.back().size(), fill);
        return result;
    }
};
