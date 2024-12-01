/* The knows API is defined for you.
      bool knows(int a, int b); */

class Solution {
public:
    int findCelebrity(int n) {
        int a = 0, b = 1;
        while(a < n && b < n) {
            if(knows(a, b)) a = max(a, b) + 1;
            else b = max(a, b) + 1;
        }
        int celeb = min(a, b);
        for(int i{}; i < n; ++i) {
            if(i == celeb) continue;
            if(!knows(i, celeb) || knows(celeb, i)) return -1;
        }
        return celeb;
    }
};
