class MovieRentingSystem {
map<pair<int, int>, int> prices;
set<tuple<int, int, int>, decltype([](auto &t1, auto &t2) -> bool {
    if(get<0>(t1) == get<0>(t2)) {
        if(get<1>(t1) == get<1>(t2)) {
            return get<2>(t1) < get<2>(t2);
        } 
        return get<1>(t1) < get<1>(t2);
    }
    return get<0>(t1) < get<0>(t2);
})> rented;
unordered_map<int, 
    set<pair<int, int>, decltype([](auto &p1, auto &p2) -> bool {
        if(get<0>(p1) == get<0>(p2)) return get<1>(p1) < get<1>(p2);
        return get<0>(p1) < get<0>(p2);
    })>
> unrented_by_movie;

public:
    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        for(auto &entry: entries) {
            int s = entry[0];
            int m = entry[1];
            int p = entry[2];
            prices[{s, m}] = p;
            unrented_by_movie[m].emplace(p, s);
        }
    }
    
    vector<int> search(int movie) {
        vector<int> result;
        auto p = unrented_by_movie[movie].begin();
        for(int i = 0; i < 5 && p != unrented_by_movie[movie].end(); ++i, ++p) {
            result.push_back(p->second);
        }
        return result;
    }
    
    void rent(int shop, int movie) {
        int p = prices[{shop, movie}];
        unrented_by_movie[movie].erase({p, shop});
        rented.emplace(p, shop, movie);
    }
    
    void drop(int shop, int movie) {
        int p = prices[{shop, movie}];
        rented.erase({p, shop, movie});
        unrented_by_movie[movie].emplace(p, shop);
    }
    
    vector<vector<int>> report() {
        vector<vector<int>> result;
        auto r = rented.begin();
        for(int i = 0; i < 5 && r != rented.end(); ++i, ++r) {
            result.push_back({get<1>(*r), get<2>(*r)});
        }
        return result;
    }
};

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem* obj = new MovieRentingSystem(n, entries);
 * vector<int> param_1 = obj->search(movie);
 * obj->rent(shop,movie);
 * obj->drop(shop,movie);
 * vector<vector<int>> param_4 = obj->report();
 */
