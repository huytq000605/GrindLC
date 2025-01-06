class Solution {
public:
    vector<int> minOperations(string boxes) {
        int right_balls{}, right_s{};
        int left_balls{}, left_s{};
        vector<int> result(boxes.size());
        for(int i{}; i < boxes.size(); ++i) {
            if(boxes[i] == '1') {
                right_balls++;
                left_s += i;
            }
        }

        for(int i{}; i < boxes.size(); ++i) {
            right_balls -= boxes[i] == '1';
            result[i] = left_s + right_s;
            left_balls += boxes[i] == '1';
            left_s += left_balls;
            right_s -= right_balls;
        }
        return result;
    }
};
