class Solution {
public:
    int maxWalls(vector<int>& robots, vector<int>& distance, vector<int>& walls) {
        int pleft = 0, pright = 0;
        vector<pair<int, int>> rds;
        for(int i = 0; i < robots.size(); ++i) rds.emplace_back(robots[i], distance[i]);
        sort(begin(rds), end(rds));
        sort(begin(walls), end(walls));
        int iwall = 0;
        int overlap = 0;
        for(int i = 0; i < rds.size(); ++i) {
            auto [robot, distance] = rds[i];
            int wleft = 0;
            int wright = 0;
            int noverlap = 0;
            for(; iwall < walls.size() && 
                    walls[iwall] <= robot + distance &&
                    (i+1 < rds.size() ? (walls[iwall] < rds[i+1].first) : true)
                ; ++iwall) {
                if(robot - distance <= walls[iwall] && walls[iwall] <= robot) {
                    ++wleft;
                }
                if(robot <= walls[iwall]) {
                    ++wright;
                }
                if(robot < walls[iwall] && i+1 < rds.size() && rds[i+1].first - rds[i+1].second <= walls[iwall]) {
                    ++noverlap;
                }
            }
            int left = wleft + max(pleft + overlap, pright);
            int right = wright + max(pleft, pright);
            pleft = left;
            pright = right;
            overlap = noverlap;
        }
        return max(pleft, pright);
    }
};
