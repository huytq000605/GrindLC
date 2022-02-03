class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        have = dict()
        need = dict()
            
        for i in range(n):
            recipe = recipes[i]
            ingredient = ingredients[i]
            need[recipe] = ingredient
            
        for supp in supplies:
            have[supp] = True
        
        def can_make(recipe):
            if recipe in have and have[recipe] == True:
                return True
            if recipe not in need:
                return False
            for ingredient in need[recipe]:
                if ingredient in have and have[ingredient] == False:
                    return False
                if ingredient not in have:
                    have[ingredient] = False
                if not can_make(ingredient):
                    return False
            have[recipe] = True
            return True
        
        result = []
        
        for r in recipes:
            if can_make(r):
                result.append(r)
        return result
