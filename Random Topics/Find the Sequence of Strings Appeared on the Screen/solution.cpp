class Solution {
public:
    vector<string> stringSequence(string target) {
        vector<string> result;
        string cur = "";
        for(int i = 0; i < target.size(); ++i) {
            char c = 'a';
            while(c != target[i]) {
                result.emplace_back(cur + c);
                c += 1;
            }
            result.emplace_back(cur + c);
            cur += c;
        }
        return result;
    }
};
