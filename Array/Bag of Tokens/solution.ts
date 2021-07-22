function bagOfTokensScore(tokens: number[], power: number): number {
    tokens.sort((a,b) => a-b)
    let score = 0
    if(power < tokens[0]) return 0
    while(tokens.length) {
        if(tokens.length && power >= tokens[0]) {
            score++
            power -= tokens[0]
            tokens.shift()
            continue
        }
        if(score > 0) {
            if(tokens.length >= 2 && tokens[0] <= tokens[tokens.length - 1] + power) {
                power = power + tokens.pop() - tokens.shift()
            } else {
                break
            }
        }
        
    }
    return score
};