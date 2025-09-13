class Solution {
public:
    int maxFreqSum(string s) {
        vector<int> f(26);
        int vowel = 0, consonant = 0;
        for(char c: s) {
            f[c - 'a']++;
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') 
                vowel = max(vowel, f[c-'a']);
            else 
                consonant = max(consonant, f[c-'a']);
        }
        return vowel + consonant;
    }
};
