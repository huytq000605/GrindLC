class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        int result = 0;
        std::sort(intervals.begin(), intervals.end());
        std::priority_queue<int, vector<int>, std::greater<int>> pq;
        for(auto i: intervals) {
            while(pq.size() > 0 && pq.top() <= i[0]) {
                pq.pop();
            }
            pq.push(i[1]);
            result = std::max<int>(result, pq.size());
        }
        return result;

    }
};
