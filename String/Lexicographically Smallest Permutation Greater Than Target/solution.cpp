class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();
        vector<int> counter(26);
        for(int i = 0; i < n; ++i) {
            counter[s[i]-'a']++;
        }
        string result;
        for(int i = 0; i < n; ++i) {
            // try to fill the same character with target until there's no equal char or it reaches the end (meaning permutations are equal)
            if(counter[target[i] - 'a'] && i != n-1) {
                counter[target[i] - 'a']--;
                result += target[i];
            } else {
                bool found = false;
                // try to find a bigger character to fill in
                for(int j = target[i] - 'a' + 1; j < 26; ++j) {
                    if(counter[j]) {
                        result += char(j + 'a');
                        found = true;
                        counter[j]--;
                        break;
                    }
                }

                // if cannot fill in a bigger character, look back
                // the earliest position we could replace result with bigger character
                if(!found) {
                    for(int j = i-1; j >= 0; --j) {
                        // remove filled character from result
                        counter[target[j] - 'a']++;
                        result.pop_back();
                        for(int k = target[j] - 'a' + 1; k < 26; ++k) {
                            
                            if(counter[k]) {
                                result += char(k + 'a');
                                found = true;
                                counter[k]--;
                                break;
                            }
                        }
                        if(found) break;
                    }
                }
                
                if(!found) return "";
                break;
            }
        }
        // after the current result is lexicographically bigger than target
        // fill the rest character
        for(int i = 0; i < 26; ++i) {
            if(counter[i]) result += string(counter[i], char(i + 'a'));
        }
        return result;
    }
};
