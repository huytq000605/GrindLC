class Solution {
public:
    int differenceOfSums(int n, int m) {
        int no_groups = n/m;
        int group = (m-1+1)*(m-1)/2 - m;
        // group + (group + m*(m-2)) + (group + m*(m-2)*2) + ... + (group + m*(m-2)*(no_groups-1) * m)
        // = group * no_groups + m*(m-2) + m*(m-2)*2 + m*(m-2)*3 + ... + m*(m-2)*(no_groups-1)
        // = group*no_groups * m*(m-2)*(no_groups)*(no_groups-1)/2
        int result = no_groups*group + no_groups*m*(m-2)*(no_groups-1)/2;
        
        int remaining = n%m;
        result += (n+(n-remaining+1)) * remaining / 2;
        return result;
        // num1 - num2
        // = (1 + 2 + .. n) - (m + 2m + .. + km) * 2
        // = (1 + n) * n / 2 - (1 + k) * k * m
        // where k = n / m (integer division)
        // return (1 + n) * n / 2 - (1 + n / m) * (n / m) * m;
    }
};
