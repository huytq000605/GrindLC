class Solution {
public:
    string findShortestWay(vector<vector<int>>& maze, vector<int>& ball, vector<int>& hole) {
        using tp = tuple<int, int, int, string>;
        priority_queue<tp, vector<tp>, decltype([](auto &t1, auto &t2) -> bool {
            if(get<0>(t1) == get<0>(t2)) {
                return get<3>(t1) > get<3>(t2);
            }
            return get<0>(t1) > get<0>(t2);
        })> pq;
        int m = maze.size(), n = maze[0].size();
        vector<vector<int>> ds(m, vector<int>(n, INT_MAX));
        ds[ball[0]][ball[1]] = 0;
        vector<tuple<int, int, string>> drc{{{1,0,"d"}, {0,-1,"l"}, {0,1,"r"}, {-1,0,"u"}}};
        pq.emplace(0, ball[0], ball[1], "");
        while(!pq.empty()) {
            auto [d, r, c, p] = pq.top(); pq.pop();
            if(r == hole[0] && c == hole[1]) return p;
            for(auto [dr, dc, dp]: drc) {
                int rr = r, cc = c, dd = d;
                bool hole_found = false;
                while(rr + dr >= 0 && rr + dr < m && 
                    cc + dc >= 0 && cc + dc < n && 
                    maze[rr + dr][cc + dc] == 0) {
                    rr += dr;
                    cc += dc;
                    ++dd;
                    if(rr == hole[0] && cc == hole[1]) {
                        hole_found = true;
                        break;
                    }
                }
                if(rr == r && cc == c) continue;
                if(dd <= ds[rr][cc] || hole_found) {
                    pq.emplace(dd, rr, cc, p + dp);
                    ds[rr][cc] = dd;
                }
            }
        };
        return "impossible";
        
    }
};
