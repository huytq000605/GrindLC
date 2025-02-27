class Solution {
public:
    long long maxScore(vector<int>& points, int m) {
        long long lo{0}, hi = pow(10, 15);
        auto valid = [&](long long k) -> bool {
            long long moves = 0;
            long long carry = 0;
            for(int i = 0; i < points.size(); ++i) {
                long long p = points[i];
                long long need = k-carry*p;
                // special case, if previous operation already fill last element
                // we dont need to move to the last element again
                if(i == points.size() - 1 && need <= 0) break;
                // move to the i element
                ++moves;
                need-=p;
                if(need > 0) {
                    long long t = (need+p-1) / p;
                    moves += 2*t;
                    carry = t;
                } else {
                    carry = 0;
                }
                if(moves > m) return false;
            }
            return true;
        };
        while(lo < hi) {
            long long k = lo + (hi - lo + 1) / 2;
            if(valid(k)) {
                lo = k;
            } else {
                hi = k-1;
            }
        }
        return lo;
    }
};
