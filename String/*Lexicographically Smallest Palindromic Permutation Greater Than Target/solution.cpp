class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.size();
        // special scenario for case n = 1
        if(n == 1) {
            if(s[0] > target[0]) return s;
            else return "";
        }
        vector<int> counter(26);
        for(char c: s) counter[c-'a']++;
        int odd = -1;
        for(int i = 0; i < 26; ++i) {
            if(counter[i] & 1) {
                if(odd != -1) return "";
                odd = i;
            }
            counter[i] >>= 1;
        }
        int m = n;
        n = n/2;
        string result;
        // satisfied = true means the first different character on the second half is larger than the character at the same index of target
        bool satisfied = false;
        for(int i = 0; i < n; ++i) {
            // try to fill the same character with target until there's no equal char or it reaches the end (meaning permutations are equal)
            if(counter[target[i] - 'a']) {
                counter[target[i] - 'a']--;
                result += target[i];
                if(target[i] > target[m-1-i]) satisfied = true;
                else if(target[i] < target[m-1-i]) satisfied = false;

                // if it's the last character on the first half
                // and none of the condition is met so that permutation is larger
                if(i == n-1 && 
                        !(
                            (odd == -1 && satisfied) || 
                            (odd != -1 && (odd > (target[m/2] - 'a'))) || 
                            (odd != -1 && (odd == (target[m/2] - 'a')) && satisfied)
                        )
                ) {
                        counter[target[i] - 'a']++;
                        result.pop_back();
                } else {
                    continue;
                }
            }

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
        // after the current result is lexicographically bigger than target
        // fill the rest character
        for(int i = 0; i < 26; ++i) {
            if(counter[i]) result += string(counter[i], char(i + 'a'));
        }
        string rresult = result;
        reverse(begin(rresult), end(rresult));
        return result + (odd != -1 ? string(1, odd + 'a'): "") + rresult;

    }
};
