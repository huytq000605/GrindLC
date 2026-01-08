class Solution {
public:
    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        vector<pair<int, int>> ds{{0,1},{1,0},{-1,0},{0,-1}};
        int m = maze.size(), n = maze[0].size();
        auto dfs = [&](this auto&& dfs, int r, int c) -> bool {
            if(r == destination[0] && c == destination[1]) return true;
            for(auto [dr, dc]: ds) {
                int rr = r, cc = c;
                bool moved = false;
                while(rr + dr >= 0 && rr + dr < m && cc + dc >= 0 && cc + dc < n && maze[rr + dr][cc + dc] != 1) {
                    rr += dr;
                    cc += dc;
                    moved = true;
                }
                if(moved && maze[rr][cc] == 0) {
                    maze[rr][cc] = -1;
                    if(dfs(rr, cc)) return true;
                }
            }
            return false;
        };

        return dfs(start[0], start[1]);
    }
};
