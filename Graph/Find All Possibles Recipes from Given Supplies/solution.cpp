class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        unordered_set<string> s(supplies.begin(), supplies.end());
        unordered_map<string, int> r;
        for(int i = 0; i < recipes.size(); ++i) {
            r[recipes[i]] = i;
        }
        unordered_set<string> cannot;
        auto possible = [&](this auto& possible, auto& u) {
            if(s.find(u) != s.end()) return true;
            if(r.find(u) == r.end() || cannot.find(u) != cannot.end()) return false;
            cannot.emplace(u);
            for(auto v: ingredients[r[u]]) {   
                if(!possible(v)) {
                    cannot.emplace(u);
                    return false;
                }
            }
            cannot.erase(u);
            s.emplace(u);
            return true;
        };
        vector<string> result;
        for(auto recipe: recipes) {
            if(possible(recipe)) result.emplace_back(recipe);
        }
        return result;
    }
};
