class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        sort(position.begin(), position.end());
        auto valid = [&](int d) {
            int prev = -1;
            int balls = 0;
            for(int p: position) {
                if(prev == -1 || prev + d <= p) {
                    balls += 1;
                    prev = p;
                }
            }
            return balls >= m;
        };

        int start = 1, end = position[position.size()-1] - position[0];
        while(start < end) {
            int d = start + ceil((end - start + 1) / 2.0);
            if(valid(d)) {
                start = d;
            } else {
                end = d - 1;
            }
        }
        return start;
    }
};
