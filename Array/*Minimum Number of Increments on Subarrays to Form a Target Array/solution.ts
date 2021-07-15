function minNumberOperations(target: number[]): number {
    let segmentTree = new SegmentTree(0, target.length - 1, 0)
    for(let i = 0; i < target.length; i++) {
        segmentTree.update(i, target[i], i)
    }
    function helper(startIdx, endIdx, initial) {
        if(startIdx > endIdx) return 0
        let node = segmentTree.query(startIdx, endIdx)
        let {min, minIdx} = node
        let result = min - initial
        let left = helper(startIdx, minIdx - 1, min)
        let right = helper(minIdx + 1, endIdx, min)
        result += left + right
        return result
    }
    return helper(0, target.length - 1, 0)
};



class SegmentTree {
    left
    right
    min
    minIdx
    start
    end
    
    constructor(start, end, minue) {
        this.start = start
        this.end = end
        this.min = minue
    }
    
    query(start, end) {
        if(start > this.end || end < this.start) {
            return null
        } 
        if(start <= this.start && end >= this.end) {
            return this
        }
        this.down()
        let left = this.left.query(start, end)
        let right = this.right.query(start, end)
        if(!left) return right
        if(!right) return left
        return left.min < right.min ? left : right
    }
    
    update(pos, minue, minIdx) {
        if(pos > this.end || pos < this.start) {
            return
        }
        if(this.start === this.end) {
            this.min = minue
            this.minIdx = minIdx
            return
        }
        this.down()
        this.left.update(pos, minue, minIdx)
        this.right.update(pos, minue, minIdx)
        if(this.left.min < this.right.min) {
            this.min = this.left.min
            this.minIdx = this.left.minIdx
        } else {
            this.min = this.right.min
            this.minIdx = this.right.minIdx
        }
    } 
    
    down() {
        if(this.start !== this.end) {
            if(!this.left || !this.right) {
                const mid = this.start + Math.floor((this.end - this.start) / 2)
                this.left = new SegmentTree(this.start, mid, 0)
                this.right = new SegmentTree(mid + 1, this.end, 0)
            }
        }
    }
}