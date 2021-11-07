function minimizedMaximum(n: number, quantities: number[]): number {
    let min = 0
    let max = Math.max(...quantities)
    
    let check = (each) => {
        let total = 0
        for(let i = 0; i < quantities.length; i++) {
            if(quantities[i] <= each) {
                total++
            } else {
                total += Math.ceil(quantities[i] / each)
            }
        }
        return total
    }
    while(min < max) {
        let mid = min + Math.floor((max - min) / 2)
        if(check(mid) <= n) {
            max = mid
        } else {
            min = mid + 1
        }
    }
    return min
    
};