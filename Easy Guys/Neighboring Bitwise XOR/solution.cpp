class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int n = derived.size();
        auto valid = [&](int first) -> bool {
            int prev{first};
            for(int i{}; i < n-1; ++i) {
                prev = prev ^ derived[i];
            }
            return first ^ prev == derived.back();
        };
        return valid(0) || valid(1);
    }
};
