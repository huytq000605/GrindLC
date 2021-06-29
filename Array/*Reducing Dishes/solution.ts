// Trick with (index + 1) * array[index], save total then plus it each time

function maxSatisfaction(satisfaction: number[]): number {
    satisfaction.sort((a,b) => a-b)
    let total = 0
    let result = 0
    for(let i = satisfaction.length - 1; total > -satisfaction[i] && i >= 0; i--) {
        /*  total need to > 0
            we have total = total + satisfaction[i]
            => total + satisfaction[i] >  0 => total > -satisfaction[i]
        */
        total += satisfaction[i]
        result += total
    }
   return result
}