function winnerOfGame(colors: string): boolean {
    let A = 0
    let B = 0
    for(let i = 1; i < colors.length - 1; i++) {
        if(colors[i] === "A" && colors[i - 1] === "A" && colors[i + 1] === "A") A++
        if(colors[i] === "B" && colors[i-1] === "B" && colors[i+1] === "B") B++
    }
    if(A > B) return true
    else return false
};