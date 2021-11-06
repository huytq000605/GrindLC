function singleNumber(nums: number[]): number[] {
    let aXORb = 0
    for(let num of nums) {
        aXORb ^= num
    }
    
    let LSB = 0
    for(let i = 0; i < 32; i++) {
        if( (aXORb & (1 << i)) !== 0) {
            LSB = 1 << i
            break
        }
    }
    
    
    let a = 0
    for(let num of nums) {
        if( (num & LSB) !== 0) {
            a ^= num
        }
    }
    
    return [a, aXORb ^ a]
};