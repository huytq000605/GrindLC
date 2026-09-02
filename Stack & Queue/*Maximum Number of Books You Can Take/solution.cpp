class Solution {
public:
    long long maximumBooks(vector<int>& books) {
        auto cal = [](long long book, long long size) {
            size = min(book, size);
            return (book + (book - size + 1)) * size / 2;
        };
        int n = books.size();
        vector<int> st;
        long long result = 0;
        for(long long i = 0, cur = 0; i < n; ++i) {
            while(!st.empty() && books[st.back()] + (i - st.back()) >= books[i]) {
                int j = st.back();
                st.pop_back();
                cur -= cal(books[j], st.empty() ? j + 1: j - st.back());
            }
            cur += cal(books[i], st.empty() ? i+1: i - st.back());
            st.push_back(i);
            result = max(result, cur);
        }
        return result;
    }
};
