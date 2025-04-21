class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        long long lowest = 0, highest = 0;
        long long acc = 0;
        for(int d: differences) {
            acc += d;
            lowest = min(lowest, acc);
            highest = max(highest, acc); 
        }
        int range = highest - lowest;
        return max(0, (upper-lower) - range + 1);
    }
};
