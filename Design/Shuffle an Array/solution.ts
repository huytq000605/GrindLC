class Solution {
    arr: number[]
    constructor(nums: number[]) {
        this.arr = nums;
    }

    reset(): number[] {
        return this.arr
    }

    shuffle(): number[] {
        let result = [...this.arr];
        for(let i = 0; i < result.length; i++) {
            const rand = Math.floor(Math.random() * result.length);
            [result[i], result[rand]] = [result[rand], result[i]]
        }
        return result
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */