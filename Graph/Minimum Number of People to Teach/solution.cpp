class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        int m = languages.size();
        vector<unordered_set<int>> langs(m);
        for(int p = 0; p < m; ++p) {
            langs[p] = unordered_set<int>(languages[p].begin(), languages[p].end());
        }
        unordered_set<int> to_teach;
        for(auto &fs: friendships) {
            int u = fs[0] - 1, v = fs[1] - 1;
            bool can_speak = false;
            for(int lang: langs[u]) {
                if(langs[v].find(lang) != langs[v].end()) {
                    can_speak = true;
                    break;
                }
            }
            if(!can_speak) {
                to_teach.insert(u);
                to_teach.insert(v);
            }
        };
        vector<int> freq_lang(n+1);
        for(int u: to_teach) {
            for(int lang: languages[u]) {
                freq_lang[lang]++;
            }
        }
        return to_teach.size() - *max_element(freq_lang.begin(), freq_lang.end());
    }
};
