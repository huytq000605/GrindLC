function minDays(bloomDay: number[], m: number, k: number): number {
    if(k*m > bloomDay.length) {
        return -1
    }
    let min = Number.MAX_SAFE_INTEGER
    let max = Number.MIN_SAFE_INTEGER
    for(let day of bloomDay) {
        min = Math.min(min, day) 
        max = Math.max(max, day) 
    }
    max = max + 1 // So middle can = max
    while(min < max) {
        let count = 0
        let bouquets = 0
        let middle = min + Math.floor((max-min)/2)
        for(let day of bloomDay) {
            if(day <= middle) {
                count++
                if(count === k) {
                    bouquets++
                    count = 0;
                    continue;
                }
            }
            
            if(day > middle) count = 0
        }
        if(bouquets < m) {
            min = middle + 1
        } else {
            max = middle
        }
    }
    return min
};