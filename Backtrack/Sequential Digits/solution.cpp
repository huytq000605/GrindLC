class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        deque<int> dq{};
        vector<int> result;
        for(int d = 1; d < 10; ++d) dq.push_back(d);
        while(!dq.empty()) {
            int num = dq.front(); dq.pop_front();
            if(low <= num && num <= high) result.push_back(num);
            int last_d = num % 10;
            if(last_d == 9) continue;
            num = num * 10 + (last_d+1);
            if(num > high) continue;
            dq.push_back(num);
        }
        return result;
    }
};
