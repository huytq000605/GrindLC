class NumArray {
    segmentTree
    constructor(nums: number[]) {
        this.segmentTree = new SegmentTree(0, nums.length - 1)
        for(let i = 0; i < nums.length; i++) {
            this.segmentTree.update(i, i, nums[i])
        }
    }

    update(index: number, val: number): void {
        this.segmentTree.update(index, index, val)
    }

    sumRange(left: number, right: number): number {
        return this.segmentTree.query(left, right)
    }
}

class SegmentTree {
    left
    right
    sum
    start
    end
    
    constructor(start, end) {
        this.start = start
        this.end = end
    }
    
    query(start, end) {
        if(start > this.end || end < this.start) {
            return 0
        }
        if(start <= this.start && end >= this.end) {
            return this.sum
        }
        this.down()
        return this.left.query(start, end) + this.right.query(start, end)
        
    }
    
    update(start, end, val) {
        if(start > this.end || end < this.start) {
            return
        }
        if(start <= this.start && end >= this.end) {
            this.sum = val
            return
        }
        this.down()
        this.left.update(start, end, val)
        this.right.update(start, end, val)
        this.sum = this.left.sum + this.right.sum
        return
    }
    
    down() {
        if(this.start < this.end) {
            if(!this.left || !this.right) {
                let mid = this.start + Math.floor((this.end - this.start)/2)
                this.left = new SegmentTree(this.start, mid)
                this.right = new SegmentTree(mid + 1, this.end)
            }
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(index,val)
 * var param_2 = obj.sumRange(left,right)
 */