class Solution {
public:
    string pushDominoes(string dominoes) {
        int n = dominoes.size();
        vector<int> next_l(n, n+1);
        vector<int> prev_r(n, n+1);

        vector<int> st;
        for(int i = 0; i < dominoes.size(); ++i) {
            if(dominoes[i] == 'L') {
                while(!st.empty()) {
                    next_l[st.back()] = i - st.back();
                    st.pop_back();
                }
            } else if(dominoes[i] == 'R') {
                st.clear();
            } else {
                st.emplace_back(i);
            }
        }

        st.clear();
        for(int i = n-1; i >= 0; --i) {
            if(dominoes[i] == 'R') {
                while(!st.empty()) {
                    prev_r[st.back()] = st.back() - i;
                    st.pop_back();
                }
            } else if(dominoes[i] == 'L') {
                st.clear();
            } else {
                st.emplace_back(i);
            }
        }

        for(int i = 0; i < n; ++i) {
            if(dominoes[i] != '.') continue;
            if(prev_r[i] < next_l[i]) dominoes[i] = 'R';
            else if(prev_r[i] > next_l[i]) dominoes[i] = 'L';
        }
        return dominoes;
    }
};
