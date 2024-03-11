class Solution {
public:
    string customSortString(string order, string s) {
        std::unordered_map<char, int> keys;
        for (int i = 0; i < order.length(); i++) {
            keys[order[i]] = i;
        }
        std::sort(s.begin(), s.end(), [keys](char c1, char c2) {
            cout << c1 << " " << c2 << "\n";
            auto key1 = keys.find(c1);
            auto key2 = keys.find(c2);
            auto v1 = key1 != keys.end() ? key1->second : 0;
            auto v2 = key2 != keys.end() ? key2->second : 0;
            return v1 < v2;
        });
        return s;
    }
};
