class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        vector<int> first(26, -1), last(26, -1);
        for(int i = 0; i < s.size(); ++i) {
            int c = s[i] - 'a';
            if(first[c] == -1) first[c] = i;
            last[c] = i;
        }

        vector<pair<int, int>> intervals;
        for(int c = 0; c < 26; ++c) {
            int l = first[c], r = last[c];
            bool valid = true;
            for(int i = l; i < r; ++i) {
                int cc = s[i] - 'a';
                int ll = first[cc], rr = last[cc];
                if(ll < l) {
                    valid = false;
                    break;
                }
                r = max(r, rr);
            }
            if(!valid) continue;
            intervals.emplace_back(l, r);
        }

        sort(begin(intervals), end(intervals), [](auto &i1, auto &i2) {
            return i1.second < i2.second;
        });
        vector<string> result;
        for(int i = 0, j = -1; i < intervals.size(); ++i) {
            auto [l, r] = intervals[i];
            if(l > j) {
                result.push_back(s.substr(l, r-l+1));
                j = l;
            }
        }
        return result;
    }
};
