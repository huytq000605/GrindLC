class Solution {
public:
    int minMaxDifference(int num) {
        string snum = to_string(num);
        char highest_swap = ' ';
        char lowest_swap = snum[0];
        int highest = 0;
        int lowest = 0;
        for(int i = 0; i < snum.size(); ++i) {
            if(highest_swap == ' ' && snum[i] != '9') highest_swap = snum[i];
            highest = highest * 10 + (snum[i] == highest_swap ? 9: snum[i] - '0');
            lowest = lowest * 10 + (snum[i] == lowest_swap ? 0: snum[i] - '0');
        }
        return highest - lowest;
    }
};
