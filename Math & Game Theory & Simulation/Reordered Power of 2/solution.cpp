class Solution {
public:
    bool reorderedPowerOf2(int n) {
        auto num_to_count = [](int num) {
            vector<int> counter(10);
            while(num) {
                counter[num % 10] += 1;
                num /= 10;
            }
            return counter;
        };

        auto pattern = num_to_count(n);
        for(int num = 1; num <= pow(10, 9); num <<= 1) {
            auto counter = num_to_count(num);
            bool valid = true;
            for(int i = 0; i < 10; i++) {
                if(counter[i] != pattern[i]) {
                    valid = false;
                    break;
                }
            }
            if(valid) return true;
        }

        return false;
    }
};
