class Solution {
public:
    long long countOfSubstrings(string word, int k) {
        auto at_least = [&word](int k) -> long long {
            map<char, int> vowels;
            auto enough_vowels = [&vowels]() -> bool {
                if(vowels.size() != 5) return false;
                for(auto [_, f]: vowels) if(f == 0) return false;
                return true;
            };
            int consonants = 0;
            long long result = 0;
            for(int i = 0, j = 0; i < word.size(); ++i) {
                if(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || 
                    word[i] == 'o' || word[i] == 'u') 
                    ++vowels[word[i]];
                else ++consonants;
                while(consonants >= k && enough_vowels()) {
                    if(word[j] == 'a' || word[j] == 'e' || word[j] == 'i' || 
                    word[j] == 'o' || word[j] == 'u') 
                        --vowels[word[j]];
                    else --consonants;
                    ++j;
                }
                result += j;
            }
            return result;
        };
        return at_least(k) - at_least(k+1);
    }
};
