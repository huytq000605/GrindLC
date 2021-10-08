function candy(ratings: number[]): number {
    let candies = Array(ratings.length).fill(1)
    for(let i = 1; i < ratings.length; i++) {
        if(ratings[i] > ratings[i-1] && candies[i] <= candies[i - 1]) {
            candies[i] = candies[i-1] + 1
        }
    }
    
    for(let i = ratings.length - 1; i >= 0; i--) {
        if(ratings[i - 1] > ratings[i] && candies[i - 1] <= candies[i]) {
            candies[i-1] = candies[i] + 1
        }
    }
    let result = 0
    for(let candy of candies) result += candy
    return result
};