class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        auto get_w1 = [](string& word) {
            string result;
            for(char c: word) {
                result += tolower(c);
            }
            return result;
        };
        auto get_w2 = [](string& word) {
            string result;
            for(char c: word) {
                c = tolower(c);
                if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                    result += '*';
                else result += c;
            }
            return result;
        };
        unordered_map<string, int> um1, um2;
        unordered_set<string> s(wordlist.begin(), wordlist.end());
        for(int i = 0; i < wordlist.size(); ++i) {
            string& w = wordlist[i];
            auto w1 = get_w1(w);
            auto w2 = get_w2(w);
            if(um1.find(w1) == um1.end()) um1[w1] = i;
            if(um2.find(w2) == um2.end()) um2[w2] = i;
        }

        vector<string> result;
        for(auto &q: queries) {
            auto q1 = get_w1(q);
            auto q2 = get_w2(q);
            if(s.find(q) != s.end()) result.push_back(q);
            else if(um1.find(q1) != um1.end()) result.push_back(wordlist[um1[q1]]);
            else if(um2.find(q2) != um2.end()) result.push_back(wordlist[um2[q2]]);
            else result.push_back("");
        }
        return result;
    }
};
