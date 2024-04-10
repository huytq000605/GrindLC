class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(deck.rbegin(), deck.rend());
        deque<int> result;
        for(auto & card: deck) {
            if(result.size() > 0) {
                result.emplace_front(result.back());
                result.pop_back();
            }
            result.push_front(card);
        }
        return vector<int>(result.begin(), result.end()); 
    }
};
