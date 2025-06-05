class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        vector<int> mapping(26, 0);
        for(int i = 0; i < 26; ++i) mapping[i] = i;
        int n = s1.size();
        auto find = [&](this auto find, int u) -> int {
            if(mapping[u] != u) mapping[u] = find(mapping[u]);
            return mapping[u];
        };
        for(int i = 0; i < n; ++i) {
            int u = find(s1[i] - 'a'), v = find(s2[i] - 'a');
            if(v < u) swap(u, v);
            mapping[v] = u;
        }
        string result;
        for(int i = 0; i < baseStr.size(); ++i) {
            result += find(baseStr[i] - 'a') + 'a';
        }
        return result;
    }
};
