class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size();
        deque<int> from, future_from;
        future_from.push_back(0);
        for(int i = 1; i < s.size(); ++i) {
            while(!future_from.empty() && i - minJump >= future_from.front()) {
                from.push_back(future_from.front());
                future_from.pop_front();
            }
            while(!from.empty() && i - maxJump > from.front()) {
                from.pop_front();
            }
            if(s[i] == '1') continue;
            if(!from.empty()) {
                if(i == n-1) return true;
                future_from.push_back(i);
            }
        }
        return false;
    }
};
