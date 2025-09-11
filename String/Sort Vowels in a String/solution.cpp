class Solution {
public:
    string sortVowels(string s) {
        unordered_map<char, int> m{{'A', 0}, {'E', 1}, {'I', 2}, {'O', 3}, {'U', 4}, {'a', 5}, {'e', 6}, {'i', 7}, {'o', 8}, {'u', 9}};
        string rm = "AEIOUaeiou";
        vector<int> freq(10, 0);
        
        for(int i = 0; i < s.size(); ++i) {
            if(m.find(s[i]) != m.end()) {
                freq[m[s[i]]] += 1;
            }
        }

        string result;
        for(int i = 0, j = 0; i < s.size(); ++i) {
            if(m.find(s[i]) != m.end()) {
                while(!freq[j]) ++j;
                result += rm[j];
                freq[j]--;
            } else {
                result += s[i];
            }
        }
        return result;
    }
};
