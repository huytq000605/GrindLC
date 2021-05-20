/*
Binary Search Question
So the capacity can be in the range of max(weights) or sum(weights)
We BST to find the answer, if we need [days] <= D then the capacity may be too high, so we decrease max
if we need [days] > D then the capacity is too low, so we increase the min
Question is asking us the minimum capacity to ship in exact D days, so even when [days] = D, still decrease max to find a more good answer
Finally the answer is when min = max; 
*/

function shipWithinDays(weights: number[], D: number): number {
    let min = 0;
    let max = 0
    for(let i = 0; i < weights.length; i++) {
        min = Math.max(min, weights[i]);
        max += weights[i]
    }
    while(min < max) {
        let capacity = Math.floor((max + min) / 2);
        let current = 0
        let days = 1;
        for(let i = 0; i < weights.length; i++) {
            current += weights[i];
            if(current > capacity) {
                days++;
                current = weights[i]
            }
        }
        if(days <= D) {
            max = capacity;
        }
        else {
            min = capacity + 1
        }
    }
    return min
    
};