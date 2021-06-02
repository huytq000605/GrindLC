function numRabbits(answers: number[]): number {
    let map = new Map()
    let result = 0
    for(let i = 0; i < answers.length; i++) {
        map.set(answers[i], (map.get(answers[i]) || 0)  + 1)
    }
    for(const [key,value] of map.entries()) {
        const numberInEachGroup = key + 1;
        let numberOfRabbits = Math.floor(value/numberInEachGroup) * numberInEachGroup;
        if(value - numberOfRabbits > 0) {
            numberOfRabbits += numberInEachGroup
        }
        result += numberOfRabbits
    }
    return result
    
};