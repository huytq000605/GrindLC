class Solution {
public:
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        using tp = tuple<int, int, int>;
        priority_queue<tp, vector<tp>, decltype([](auto &t1, auto &t2) -> bool {
            return get<0>(t1) > get<0>(t2);
        })> pq;
        int m = maze.size(), n = maze[0].size();
        vector<vector<int>> ds(m, vector<int>(n, INT_MAX));
        ds[start[0]][start[1]] = 0;
        vector<pair<int, int>> drc{{{0,1}, {1,0}, {0,-1}, {-1,0}}};
        pq.emplace(0, start[0], start[1]);
        while(!pq.empty()) {
            auto [d, r, c] = pq.top(); pq.pop();
            if(r == destination[0] && c == destination[1]) return d;
            for(auto [dr, dc]: drc) {
                int rr = r, cc = c, dd = d;
                while(rr + dr >= 0 && rr + dr < m && 
                    cc + dc >= 0 && cc + dc < n && maze[rr + dr][cc + dc] == 0) {
                    rr += dr;
                    cc += dc;
                    ++dd;
                }
                if(dd < ds[rr][cc]) {
                    pq.emplace(dd, rr, cc);
                    ds[rr][cc] = dd;
                }
            }
        };
        return -1;
    }
};
