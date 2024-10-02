class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<pair<int, int>> A;
        for(int i = 0; i < arr.size(); ++i) A.emplace_back(i, arr[i]);
        sort(A.begin(), A.end(), [](auto &p1, auto &p2) {
            return p1.second < p2.second;
        });
        vector<int> result(arr.size(), 0);
        for(int i = 0, r = 1; i < A.size(); ++i) {
            if(i && A[i-1].second != A[i].second) ++r;
            result[A[i].first] = r;
        }
        return result;
    }
};
