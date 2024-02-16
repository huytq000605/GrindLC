function findLeastNumOfUniqueInts(arr: number[], k: number): number {
    let counter = new Map()
    let removed = 0
    for(let i = 0; i < arr.length; i++) {
        if(!counter.get(arr[i])) {
            counter.set(arr[i], 1)
        } else {
            counter.set(arr[i], counter.get(arr[i]) + 1)
        }
    }
    let uniqueInts = counter.size
    let freqs = []
    for(let value of counter.values()) {
        freqs.push(value)
    }
    freqs.sort((a,b) => a-b);
    for(let freq of freqs) {
        if(freq > k) {
            break
        } else {
            k-=freq
            removed++
        }
    }
    return uniqueInts - removed
};