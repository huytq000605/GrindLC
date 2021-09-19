// O(n + klogn)
function mostCompetitive(nums: number[], k: number): number[] {
    let result = []
    let segmentTree = new SegmentTree(0, nums.length - 1, 0)
    for(let i = 0; i < nums.length; i++) {
        segmentTree.update(i, i, nums[i])
    }
    function helper(startIndex: number, k: number) {
        if(k === 0) return
        let min = segmentTree.query(startIndex, nums.length - k)
        result.push(min[0])
        helper(min[1] + 1, k - 1)
    }
    helper(0, k)
    return result
};

class SegmentTree {
    start
    end
    left
    right
    min
    index
    
    constructor(start, end, min) {
        this.start = start
        this.end = end
        this.min = min
    }
    
    query(start, end) {
        if(this.start > end || this.end < start) {
            return [Number.MAX_SAFE_INTEGER, - 1]
        }
        
        if(this.start >= start && this.end <= end) {
            return [this.min, this.index]
        }
        this.down()
        const left = this.left.query(start, end)
        const right = this.right.query(start, end)
        if(left[0] <= right[0]) {
            return left
        } else {
            return right
        }
    }
    
    update(pos, index, value) {
        if(this.start > pos || this.end < pos) {
            return
        }
        if(this.start === this.end) {
            this.min = value
            this.index = index
            return
        }
        this.down()
        this.left.update(pos, index,value)
        this.right.update(pos, index, value)
        if(this.left.min <= this.right.min) {
            this.min = this.left.min
            this.index = this.left.index
        } else {
            this.min = this.right.min
            this.index = this.right.index
        }
        
    }
    
    down() {
        if(this.start !== this.end) {
            if(!this.left || !this.right) {
                const mid = this.start + Math.floor((this.end - this.start)/ 2)
                this.left = new SegmentTree(this.start, mid, this.min)
                this.right = new SegmentTree(mid + 1, this.end, this.min)
            }
        }
    }
}