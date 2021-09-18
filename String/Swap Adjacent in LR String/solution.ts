// After deleting "X", we must get the same string
function canTransform(start: string, end: string): boolean {
    if(start.length !== end.length) return false
    let from = ""
    let to = ""
    for(let i = 0; i < start.length; i++) {
        if(start[i] !== "X") from += start[i]
        if(end[i] !== "X") to += end[i]
    }
    if(from !== to) return false
    let startLeft = 0
    let startRight = 0
    let endLeft = 0
    let endRight = 0
    for(let i = 0; i < start.length; i++) {
        if(start[i] === "L") startLeft++
        if(end[i] === "L") endLeft++
        if(start[i] === "R") startRight++
        if(end[i] === "R") endRight++
        if(startLeft > endLeft) return false
        if(startRight < endRight) return false
    }
    return true
};