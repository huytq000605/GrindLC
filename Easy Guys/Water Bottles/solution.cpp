class Solution {
public:
    int numWaterBottles(int bottles, int exchange) {
        int result = 0;
        int empty = 0;
        while(bottles) {
            result += bottles;
            int nempty = (bottles + empty) % exchange;
            bottles = (bottles + empty) / exchange;
            empty = nempty;
        }
        return result;
    }
};
