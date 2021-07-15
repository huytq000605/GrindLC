function sampleStats(count: number[]): number[] {
    let min = -1
    let max = -1
    let sum = 0
    let ele = 0
    let mode = [0, -1]
    for(let i = 0; i < count.length; i++) {
        if(count[i] !== 0) {
            if(min === -1) min = i
            max = i
            sum += count[i] * i
            ele += count[i]
            if(mode[1] === -1) mode = [count[i], i]
            if(mode[0] < count[i]) mode = [count[i], i]
        }
    }
    let mean = sum / ele
    let m1 = Math.floor(ele / 2) // index of median 1
    let m2 = ele % 2 === 0 ? m1 - 1 : m1 // index of median 2
    let c = 0 // index
    let median = 0
    for(let i = 0; i < count.length; i++) {
        if(c <= m1 && c + count[i] > m1) {
            median += i / 2
            m1 = -1
        }
        if(c <= m2 && c + count[i] > m2) {
            median += i / 2
            m2 = -1
        }
        c += count[i]
        
    }
    return [min, max, mean, median, mode[1]]
};