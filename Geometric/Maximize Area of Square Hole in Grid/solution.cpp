class Solution {
public:
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        int result = 1;
        sort(begin(hBars), end(hBars));
        sort(begin(vBars), end(vBars));
        auto max_length = [](vector<int>& sides) {
            int length = 2;
            int ret = length;
            for(int i = 1; i < sides.size(); ++i) {
                if(sides[i-1] + 1 == sides[i]) ++length;
                else length = 2;
                ret = max(ret, length);
            }
            return ret;
        };
        int l = min(max_length(hBars), max_length(vBars));
        return l*l;
    }
};
