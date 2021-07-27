function getHint(secret: string, guess: string): string {
    let map = new Map()
    let used = new Set()
    for(let num of secret) {
        map.set(num, (map.get(num) || 0) + 1)
    }
    let result = [0, 0]
    for(let i = 0; i < guess.length; i++) {
        if(guess[i] === secret[i]) {
            used.add(i)
            result[0]++
            map.set(guess[i], map.get(guess[i]) - 1)
        } 
    }
    
    for(let i = 0; i < guess.length; i++) {
        if(!used.has(i) && map.has(guess[i]) && map.get(guess[i]) > 0) {
            result[1]++
            map.set(guess[i], map.get(guess[i]) - 1)
        }
    }
    return `${result[0]}A${result[1]}B`
};