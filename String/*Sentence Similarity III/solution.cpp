class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        auto split = [](string s) -> vector<string> {
            vector<string> result;
            string cur;
            for(char c: s) {
                if(c == ' ') {
                    result.emplace_back(cur);
                    cur = "";
                } else cur += c;
            }
            if(!cur.empty()) result.emplace_back(cur);
            return result;
        };

        auto s1 = split(sentence1);
        auto s2 = split(sentence2);
        if(s1.size() > s2.size()) swap(s1, s2);
        int i = 0, j = s1.size()-1, diff = s2.size() - s1.size();
        while(i < s1.size() && i < s2.size() && s1[i] == s2[i]) ++i;
        if(i == s1.size()) return true;
        while(j >= i && s2[j + diff] == s1[j]) j--;
        return i > j;
    }
};
