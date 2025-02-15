class Solution {
public:
    int punishmentNumber(int n) {
        int result{};
        auto can_partition = [](this auto can_partition, string num, int target) {
            if(stoi(num) == target) return true;
            for(int i{1}; i < num.size(); ++i) {
                if(can_partition(num.substr(i), target - stoi(num.substr(0, i))))
                    return true;
            }
            return false;
        };
        for(int i = 1; i <= n; ++i) {
            int sq = i*i;
            if(can_partition(to_string(sq), i)) result += sq;
        }
        return result;
    }
};
