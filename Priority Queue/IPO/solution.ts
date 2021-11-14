function findMaximizedCapital(k: number, w: number, profits: number[], capital: number[]): number {
    let projects = profits.map((e, i) => [e, capital[i]])
    projects.sort((a,b) => a[1] - b[1])
    let canDo = new MinHeap((a,b) => {
        if(a > b) return -1
        if(a === b) return 0
        return 1
    })
    let idx = 0
    while(k > 0) {
        while(idx < projects.length && projects[idx][1] <= w) {
            canDo.push(projects[idx][0])
            idx++
        }
        if(!canDo.length) break
        w += canDo.pop()
        k--
    }
    return w
};


class MinHeap {
    arr
    cmp
    constructor(cmp) {
        this.arr = []
        this.cmp = cmp
    }
    
    get length() {
        return this.arr.length
    }
    
    push(val) {
        this.arr.push(val)
        this.bubbleUp()
    }
    
    pop() {
        [this.arr[this.arr.length-1], this.arr[0]] = [this.arr[0], this.arr[this.arr.length - 1]];
        let popValue = this.arr.pop()
        this.bubbleDown()
        return popValue
    }
    
    bubbleUp() {
        let current = this.arr.length - 1
        while(current > 0) {
            let parent = Math.floor((current - 1) / 2)
            if(this.cmp(this.arr[current], this.arr[parent]) === -1) {
                [this.arr[current], this.arr[parent]] = [this.arr[parent], this.arr[current]];
                current = parent
            } else {
                break
            }
        }
    }
    
    bubbleDown() {
        let current = 0
        while(true) {
            let left = current * 2 + 1
            if(left >= this.arr.length) return
            let right = left + 1
            if(right >= this.arr.length) right = left
            let smaller = 0
            if(this.cmp(this.arr[left], this.arr[right]) === -1) {
                smaller = left
            } else {
                smaller = right
            }
            if(this.cmp(this.arr[smaller], this.arr[current]) === -1) {
                [this.arr[smaller], this.arr[current]] = [this.arr[current], this.arr[smaller]];
                current = smaller
            } else {
                break
            }
        }
    }
}