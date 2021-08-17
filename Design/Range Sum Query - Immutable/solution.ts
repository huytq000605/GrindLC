class NumArray {
    prefix
    constructor(nums: number[]) {
        this.prefix = Array(nums.length)
        for(let i = 0; i < nums.length; i++) {
            if(i === 0) this.prefix[0] = nums[0]
            else this.prefix[i] = this.prefix[i-1] + nums[i]
        }
    }

    sumRange(left: number, right: number): number {
        if(left === 0) {
            return this.prefix[right]
        } else {
            return this.prefix[right] - this.prefix[left - 1]
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */