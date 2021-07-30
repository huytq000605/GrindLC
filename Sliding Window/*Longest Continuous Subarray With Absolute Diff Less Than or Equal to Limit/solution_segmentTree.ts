function longestSubarray(nums: number[], limit: number): number {
    let start = 0
    let result = 0
    let minTree = new SegmentTree(0, nums.length - 1, Math.min)
    let maxTree = new SegmentTree(0, nums.length - 1, Math.max)
    for(let [idx, num] of nums.entries()) {
        minTree.update(idx, num)
        maxTree.update(idx, num)
    }
    for(let end = 0; end < nums.length; end++) {
        let min = minTree.query(start, end)
        let max = maxTree.query(start, end)
        let diff = max - min
        while(diff > limit && start <= end) {
            start++
            min = minTree.query(start, end)
            max = maxTree.query(start, end)
            diff = max - min
        }
        if(start > end) continue
        result = Math.max(result, end - start + 1)
    }
    return result
};

class SegmentTree {
    left
    right
    start
    end
    val
    fn
    
    constructor(start, end, fn) {
        this.start = start
        this.end = end
        this.fn = fn
        if(this.fn === Math.max) {
            this.val = Number.MIN_SAFE_INTEGER
        } else {
            this.val = Number.MAX_SAFE_INTEGER
        }
    }
    
    query(start, end) {
        if(start > this.end || end < this.start) {
            if(this.fn === Math.max) {
                return Number.MIN_SAFE_INTEGER
            } else {
                return Number.MAX_SAFE_INTEGER
            }
        }
        if(this.start >= start && end >= this.end) {
            return this.val
        }
        this.down()
        let left = this.left.query(start, end)
        let right = this.right.query(start, end)
        return this.fn(left, right)
    }
    
    update(position, val) {
        if(position > this.end || position < this.start) {
            return
        }
        if(this.start === this.end) {
            this.val = val
            return
        }
        this.down()
        this.left.update(position, val)
        this.right.update(position, val)
        this.val = this.fn(this.left.val, this.right.val)
        
    }
    
    down() {
        if(this.start !== this.end) {
            if(!this.left || !this.right) {
                const middle = this.start + Math.floor((this.end - this.start) / 2)
                this.left = new SegmentTree(this.start, middle, this.fn)
                this.right = new SegmentTree(middle + 1, this.end, this.fn)
            }
        }
    }
}