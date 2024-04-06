class Solution {
public:
    int maxBottlesDrunk(int bottles, int exchange) {
        int result = 0;
        int empty = 0;
        while(bottles) {
            result += bottles;
            empty += bottles;
            bottles = 0;
            if(empty >= exchange) {
                bottles += 1;
                empty -= exchange++;
            }
        }
        return result;
    }
};
