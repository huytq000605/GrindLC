vector<int> prime_idxs{2,3,5,7,11,13,17,19};
vector<bool> primes(20);

class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        if(!primes[2]) for(int i: prime_idxs) primes[i] = true;

        int result = 0;
        for(uint num = left; num <= right; ++num) {
            int set_bits = std::popcount(num);
            if(primes[set_bits]) ++result;
        }
        return result;
    }
};
