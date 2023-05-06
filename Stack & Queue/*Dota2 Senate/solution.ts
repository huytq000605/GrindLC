function predictPartyVictory(senate: string): string {
    let r = []
    let d = []
    for(let i = 0; i < senate.length; i++) {
        if(senate[i] === "R") r.push(i)
        else d.push(i)
    }
    while(r.length && d.length) {
        let next1 = r.shift()
        let next2 = d.shift()
        if(next1 < next2) {
            r.push(next1 + senate.length)
        } else {
            d.push(next2 + senate.length)
        }
        
    }
    return r.length ? "Radiant" : "Dire"
};