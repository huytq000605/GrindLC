/*
// Definition for an Interval.
class Interval {
public:
    int start;
    int end;

    Interval() {}

    Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Solution {
public:
    vector<Interval> employeeFreeTime(vector<vector<Interval>> schedule) {
        vector<Interval> result;
        int prev = INT_MIN;
        int n = schedule.size();
        priority_queue<tuple<int, int, int, int>,
            vector<tuple<int, int, int, int>>,
            greater<>> pq;
        for(int i = 0; i < n; ++i)  {
            pq.emplace(schedule[i][0].start, schedule[i][0].end, i, 0);
        }
        int last_end = INT_MIN;
        while(!pq.empty()) {
            auto [start, end, s, i] = pq.top(); pq.pop();
            ++i;
            if(i < schedule[s].size()) {
                pq.emplace(schedule[s][i].start, schedule[s][i].end, s, i);
            }
            if(last_end < start && last_end != INT_MIN) {
                result.emplace_back(last_end, start);
            }
            last_end = max(last_end, end);
        }
        return result;
    }
};
