function singleNumber(nums: number[]): number {
    let arrayBit = Array(32).fill(0)
    
    let addNum = (num) => {
        for(let i = 0; i < 32; i++) {
            if(num & (1 << i)) arrayBit[i]++
        }    
    }
    
    for(let num of nums) {
        addNum(num)
    }
    
    let result = 0
    for(let i = 0; i < arrayBit.length; i++) {
        if(arrayBit[i] % 3 !== 0) {
            result |= (1 << i)
        }
    }
    return result
};