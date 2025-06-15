class Solution {
public:
    int maxDiff(int num) {
        string snum = to_string(num);
        char highest_swap = ' ', lowest_swap = snum[0] == '1' ? ' ': snum[0];
        int highest = 0, lowest = 0;
        for(int i = 0; i < snum.size(); ++i) {
            if(highest_swap == ' ' && snum[i] != '9') highest_swap = snum[i];
            if(lowest_swap == ' ' && snum[i] != snum[0] && snum[i] != '0') lowest_swap = snum[i];
            highest = highest * 10 + (snum[i] == highest_swap ? 9: snum[i] - '0');
            lowest = lowest * 10 + (snum[i] == lowest_swap ? (snum[i] == snum[0] ? 1: 0): snum[i] - '0');
        }

        return highest - lowest;
    }
};
