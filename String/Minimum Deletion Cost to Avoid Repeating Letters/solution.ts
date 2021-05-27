/*
First we have a hash map, we loop through all characters of the string from index 1
We create an key is a number increment each time we dont have a group
If we caught a letter same as previous letter, so we save both of it to hash map as a group but dont increase the key, if the next char is still the same letter as 2(or more) previous, so that number will be in the same group ...
After all, we get all the group of same identical letter
The cost we must pay is sum of a group - max of a group
*/

function minCost(s: string, cost: number[]): number {
    let map = new Map()
    let key = 0
    let result = 0;
    for(let i = 1; i < s.length; i++) {
        if(s[i-1] === s[i]) {
            if(!map.has(key)) map.set(key, [cost[i-1], cost[i]])
            else map.get(key).push(cost[i]);
        }
        else {
            key++
        }
    }
    for(let value of map.values()) {
            let max = 0
            for(let each of value) {
                max = Math.max(max, each);
                result += each;
            }
            result -= max;
    }
    return result
    
};  