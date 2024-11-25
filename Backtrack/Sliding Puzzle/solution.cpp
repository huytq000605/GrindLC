class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        vector<vector<int>> ds{{}, {2, 4}, {1,3,5}, {2, 6}, {1, 5}, {2, 4, 6}, {3, 5}};
        unordered_set<string> seen;
        string state{"6"};
        int m = board.size(), n = board[0].size();
        for(int r{}; r < m; ++r) {
            for(int c{}; c < n; ++c) {
                state += (board[r][c] + '0');
            }
        }
        
        deque<string> dq;
        dq.emplace_back(state);
        seen.emplace(state);
        int result{};
        while(!dq.empty()) {
            int l = dq.size();
            for(int i{}; i < l; ++i) {
                state = dq.front();
                dq.pop_front();
                if(state == "6123450") return result;
                int u = state.find('0');
                for(int v: ds[u]) {
                    swap(state[u], state[v]);
                    if(seen.find(state) == seen.end()) {
                        seen.emplace(state);
                        dq.emplace_back(state);
                    }
                    swap(state[u], state[v]);
                }
            }
            ++result;
        }
        
        return -1;
    }
};
