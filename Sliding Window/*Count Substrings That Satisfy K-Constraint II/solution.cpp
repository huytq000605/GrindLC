class Solution {
public:
    vector<long long> countKConstraintSubstrings(string s, int k, vector<vector<int>>& queries) {
        int n = s.size();
        vector<int> left_to_right(n, 0);
        vector<int> right_to_left(n, 0);

        for(int i = 0, j = 0, zeros = 0, ones = 0; i < n; i++) {
            zeros += s[i] == '0';
            ones += s[i] == '1';
            while(zeros > k && ones > k) {
                zeros -= s[j] == '0';
                ones -= s[j] == '1';
                j++;
            }
            right_to_left[i] = j;
        }

        for(int i = n-1, j = n-1, zeros = 0, ones = 0; i >= 0; --i) {
            zeros += s[i] == '0';
            ones += s[i] == '1';
            while(zeros > k && ones > k) {
                zeros -= s[j] == '0';
                ones -= s[j] == '1';
                --j;
            }
            left_to_right[i] = j;
        }

        vector<long long> prefix(n, 0);
        for(int i = 0; i < n; i++) {
            long long l = i - right_to_left[i] + 1;
            prefix[i] = (i > 0 ? prefix[i-1] : 0) + l;
        }
        vector<long long> result;
        for(auto q: queries) {
            int l = q[0], r = q[1];
            int m = min(r, left_to_right[l]);
            long long res = 0;
            // all the substr ends in [l:m+1] will be k-constraint
            res += static_cast<long long>(m - l + 1) * (m - l + 2) / 2;
            // for substr ends in [m+1: r], left will be >= right_to_left[end]
            // for(int end = r; end > m; end--) res += end - right_to_left[end] + 1
            res += prefix[r] - prefix[m];
            result.emplace_back(res);
        }
        return result;
    }
};
