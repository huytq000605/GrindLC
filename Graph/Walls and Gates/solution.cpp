class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int m = rooms.size(), n = rooms[0].size();
        deque<tuple<int, int, int>> dq;
        for(int r = 0; r < m ; ++r) {
            for(int c = 0; c < n; ++c) {
                if(rooms[r][c] == 0) {
                    dq.emplace_back(0, r, c);
                }
            }
        }
        vector<pair<int, int>> drc{{0,1},{1,0},{-1,0},{0,-1}};
        while(!dq.empty()) {
            auto [s, r, c] = dq.front(); dq.pop_front();
            for(auto [dr, dc]: drc) {
                int nr = r + dr, nc = c + dc;
                if(nr < 0 || nr >= m || nc < 0 || nc >= n || rooms[nr][nc] == -1 || rooms[nr][nc] < INT_MAX) continue;
                rooms[nr][nc] = s + 1;
                dq.emplace_back(s+1, nr, nc); 
            }
        }
    }
};
