function checkValidString(s: string): boolean {
    let openMax = 0
    let openMin = 0
    for(let i = 0; i < s.length; i++) {
        if(s[i] === "(") {
            openMax++
            openMin++
        } else if(s[i] === ")") {
            openMax--
            openMin--
        } else {
            openMax++
            openMin--
        }
        if(openMax < 0) return false // There's not enough "(" + "*" to match with ")"
        openMin = Math.max(0, openMin) // We cannot let openMin < 0
    }
    if(openMin > 0) return false
    return true
};