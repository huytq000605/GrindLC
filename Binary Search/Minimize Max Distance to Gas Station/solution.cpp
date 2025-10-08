class Solution {
public:
    double minmaxGasDist(vector<int>& stations, int k) {
        double lo = 0, hi = stations.back() - stations.front();
        auto valid = [k, &stations](double m) {
            int l = k;
            for(int i = 0; i < stations.size() - 1; ++i) {
                double gap = stations[i+1] - stations[i];
                l -= ceil(gap / m) - 1;
                if(l < 0) return false;
            }
            return true;
        };
        while(lo + 1e-6 < hi) {
            double mi = lo + (hi - lo) / 2;
            if(valid(mi)) {
                hi = mi;
            } else {
                lo = mi;
            }
        }
        return lo;
    }
};
