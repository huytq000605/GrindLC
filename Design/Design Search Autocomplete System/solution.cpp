class AutocompleteSystem {
    vector<string> strs;
    unordered_map<string, int> counter;
    vector<string> cur;
    string cur_str;
public:
    AutocompleteSystem(vector<string>& sentences, vector<int>& times) {
        for(int i = 0; i < sentences.size(); ++i) {
            strs.push_back(sentences[i]);
            counter[sentences[i]] = times[i];
        }
        cur = strs;
    }
    
    vector<string> input(char c) {
        if(c == '#') {
            if(counter.find(cur_str) == counter.end()) strs.push_back(cur_str);
            counter[cur_str]++;
            cur_str = "";
            cur = strs;
            return {};
        }
        vector<string> ncur;
        int i = cur_str.size();
        for(auto &s: cur) {
            if(i < s.size() && s[i] == c) {
                ncur.push_back(s);
            }
        }
        cur_str += c;
        sort(begin(ncur), end(ncur), [this](auto &s1, auto &s2) -> bool {
            if(counter[s1] == counter[s2]) return s1 < s2;
            return counter[s1] > counter[s2];
        });
        cur = ncur;

        vector<string> res;
        for(int i = 0; i < min(3, int(cur.size())); ++i) {
            res.push_back(cur[i]);
        }
        return res;
    }
};

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem* obj = new AutocompleteSystem(sentences, times);
 * vector<string> param_1 = obj->input(c);
 */
