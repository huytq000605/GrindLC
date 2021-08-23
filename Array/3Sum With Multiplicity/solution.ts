function threeSumMulti(arr: number[], target: number): number {
    let freq = new Map()
    let result = 0
    const MOD = 1e9 + 7
    for(let num of arr) {
        freq.set(num, (freq.get(num) || 0) + 1)
    }
    for(let i = 0; i < arr.length - 2; i++) {
        freq.set(arr[i], freq.get(arr[i]) - 1)
        for(let j = i + 1; j < arr.length - 1; j++) {  
            freq.set(arr[j], freq.get(arr[j]) - 1)
            result += freq.get(target - arr[i] - arr[j]) || 0   
            result = result % MOD
        }
        
        for(let j = i + 1; j < arr.length - 1; j++) {
            freq.set(arr[j], freq.get(arr[j]) + 1)
        }
    }
    return result
};