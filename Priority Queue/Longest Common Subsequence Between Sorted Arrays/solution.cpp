class Solution {
public:
    vector<int> longestCommonSubsequence(vector<vector<int>>& arrays) {
        vector<int> result;
        priority_queue<tuple<int, int, int>, 
            vector<tuple<int, int, int>>, 
            decltype([](auto a, auto b) -> bool {
                return get<0>(a) > get<0>(b);
            })> pq;
        // {value, idx of the list, idx in the list}
        for(int i = 0; i < arrays.size(); i++) {
            pq.emplace(make_tuple(arrays[i][0], i, 0));
        }
        while(pq.size() == arrays.size()) {
            int value = get<0>(pq.top());
            int popped = 0;
            while(!pq.empty() && get<0>(pq.top()) == value) {
                auto [_, i, j] = pq.top();
                pq.pop();
                if(j + 1 < arrays[i].size()) {
                    pq.emplace(make_tuple(arrays[i][j+1], i, j+1));
                }
                popped += 1;
            }
            if(popped == arrays.size()) {
                result.emplace_back(value);
            }
        }
        return result;
    }
};
