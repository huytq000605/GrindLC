class Solution {
public:
    int numberOfCleanRooms(vector<vector<int>>& room) {
        int m = room.size(), n = room[0].size();
        set<pair<int, pair<int, int>>> s;
        vector<pair<int, int>> ds = {{0,1}, {1,0}, {0, -1}, {-1, 0}};
        int di = 0, r = 0, c = 0;
        int result = 0;
        while(1) {
            if(s.find({di, {r, c}}) != s.end()) break;
            s.emplace(di, make_pair(r, c));
            if(room[r][c] == 0) {
                result += 1;
                room[r][c] = -1;
            }
            auto [dr, dc] = ds[di];
            int nr = r + dr, nc = c + dc;
            if(nr < 0 || nr >= m || nc < 0 || nc >= n || room[nr][nc] == 1) {
                di = (di + 1) % ds.size();
            } else {
                r = nr;
                c = nc;
            }
        }
        return result;
    }
};
