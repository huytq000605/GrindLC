class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        double lo{0}, hi{pow(10, 9)};
        const double eps = pow(10,-5);
        auto cmp = [&](double yk) {
            double above{}, below{};
            for(auto& sq: squares) {
                double x = sq[0], y = sq[1], l = sq[2];
                above += max(min((y+l) - yk, l), 0.0) * l;
                below += max(min(yk - y, l), 0.0) * l;
            }
            return above <= below;
        };
        while(lo < hi - eps) {
            double y = lo + (hi - lo) / 2.0;
            if(!cmp(y)) {
                lo = y;
            } else {
                hi = y;
            }
        }
        return lo;
    }
};
