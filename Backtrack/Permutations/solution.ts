function permute(nums: number[]): number[][] {
    let freq = new Map()
    let result = []
    for(let num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1)
    }
    construct([], result, freq, nums.length)
    return result
};

function construct(current: number[],result: number[][], freq: Map<number, number>, length: number) {
    if(current.length == length) {
        result.push([...current])
        return
    }
    for(let [key, value] of freq.entries()) {
        if(value == 0) continue;
        current.push(key)
        freq.set(key, value - 1)
        construct(current, result, freq, length)
        freq.set(key, value)
        current.pop()
    }
}