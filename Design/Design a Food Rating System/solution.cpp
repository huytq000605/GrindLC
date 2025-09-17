class FoodRatings {
unordered_map<string, priority_queue<pair<string, int>, vector<pair<string, int>>, decltype([](auto &p1, auto &p2) -> bool {
    if(p1.second == p2.second) {
        return p1.first > p2.first;
    }
    return p1.second < p2.second;
})>> um_pq;
unordered_map<string, int> ratings;
unordered_map<string, string> food_cuisine;
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for(int i = 0; i < foods.size(); ++i) {
            string f = foods[i];
            string c = cuisines[i];
            int r = ratings[i];
            um_pq[c].emplace(f, r);
            this->ratings[f] = r;
            food_cuisine[f] = c;
        }
    }
    
    void changeRating(string food, int newRating) {
        ratings[food] = newRating;
        string cuisine = food_cuisine[food];
        um_pq[cuisine].emplace(food, newRating);
    }
    
    string highestRated(string cuisine) {
        while(true) {
            auto [f, r] = um_pq[cuisine].top();
            if(ratings[f] == r) break;
            um_pq[cuisine].pop();
        }
        return um_pq[cuisine].top().first;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */
