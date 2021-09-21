function maxValue(n: string, x: number): string {
    let negative = false
    if(n[0] === "-") negative = true
    if(!negative) {
        for(let i = 0; i < n.length; i++) {
            let digit = Number(n[i])
            if(digit < x) {
                return n.slice(0, i) + x + n.slice(i)
            }
        }
    } else {
        for(let i = 1; i < n.length; i++) {
            let digit = Number(n[i])
            if(digit > x) {
                return n.slice(0, i) + x + n.slice(i)
            }
        }
    }
    return n + x
};