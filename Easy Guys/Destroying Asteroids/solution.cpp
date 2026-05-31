class Solution {
public:
    bool asteroidsDestroyed(long long mass, vector<int>& asteroids) {
        sort(begin(asteroids), end(asteroids));
        for(int a: asteroids) {
            if(mass < a) return false;
            mass += a;
        }
        return true;
    }
};
