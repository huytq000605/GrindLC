class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        int last = 0;
        int result = 0;
        sort(meetings.begin(), meetings.end());
        for(auto& m: meetings) {
            int s = m[0], e = m[1];
            if(last < s) {
                result += s - last - 1;
            }
            last = max(last, e);
        }
        return result + days - last;
    }
};
