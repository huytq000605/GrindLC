function predictPartyVictory(senate: string): string {
    let r = 0
    let d = 0
    let banR = 0
    let banD = 0
    for(let l of senate) {
        if(l === "R") r++
        else d++
    }
    if(r===0) return "Dire"
    if(d===0) return "Radiant"
    let remove = new Set()
    for(let i = 0; ; i++) {
        i = i % senate.length
        if(remove.has(i)) continue
        if(senate[i] === "D" && banD) {
            banD--
            remove.add(i)
            continue
        }
        if(senate[i] === "R" && banR) {
            banR--
            remove.add(i)
            continue
        }
        if(senate[i] === "D") {
            r--
            banR++
            if(r===0) return "Dire"
        } else {
            d--
            banD++
            if(d===0) return "Radiant"
        }
    }
};