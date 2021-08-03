function getNumberOfBacklogOrders(orders: number[][]): number {
    let buyBackLog = new MinHeap((a,b) => {
        if(a[0] > b[0]) return -1
        if(a[0]===b[0]) return 0
        return 1
    })
    let sellBackLog = new MinHeap((a,b) => {
        if(a[0]>b[0]) return 1
        if(a[0]===b[0]) return 0
        return -1
    })
    for(let [price, amount, type] of orders) {
        if(type === 0) { // buy
            while(amount > 0 && sellBackLog.length > 0) {
                let minSell = sellBackLog.pop()
                if(minSell[0] > price) {
                    sellBackLog.push(minSell)
                    break
                } else {
                    let use = Math.min(minSell[1], amount)
                    minSell[1] -= use
                    amount -= use
                }
                if(minSell[1] > 0) {
                    sellBackLog.push(minSell)
                }
            }
            if(amount > 0) {
                buyBackLog.push([price, amount])
            }
        } else {
            while(amount > 0 && buyBackLog.length > 0) {
                let maxBuy = buyBackLog.pop()
                if(maxBuy[0] < price) {
                    buyBackLog.push(maxBuy)
                    break
                } else {
                    let use = Math.min(maxBuy[1], amount)
                    maxBuy[1] -= use
                    amount -= use
                }
                if(maxBuy[1] > 0) {
                    buyBackLog.push(maxBuy)
                }
            }
            if(amount > 0) {
                sellBackLog.push([price, amount])
            }
        }
    }
    
    let result = 0
    while(sellBackLog.length) {
        let [price, amount] = sellBackLog.pop()
        result += amount % (1e9 + 7)
        result = result % (1e9 + 7)
    }
    while(buyBackLog.length) {
        let [price, amount] = buyBackLog.pop()
        result += amount % (1e9 + 7)
        result = result % (1e9 + 7)
        
    }
    return result
    
};

class MinHeap {
    arr
    cmp
    
    constructor(fn) {
        this.arr = []
        this.cmp = fn
    }
    
    
    push(ele) {
        this.arr.push(ele)
        this.bubbleUp()
    }
    
    get length() {
        return this.arr.length
    }
    
    pop() {
        if(this.length > 0) {
            [this.arr[0], this.arr[this.arr.length - 1]] = [this.arr[this.arr.length - 1], this.arr[0]];
            let pop = this.arr.pop()
            this.bubbleDown()
            return pop
        } else {
            return undefined
        }
    }
    
    bubbleUp() {
        let current = this.arr.length - 1
        while(current > 0) {
            let parent = Math.ceil(current / 2) - 1
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
            let left = current * 2  +1
            if(left > this.arr.length -  1) return
            let right = left + 1
            if(right > this.arr.length - 1) right = left
            let smaller
            if(this.cmp(this.arr[left], this.arr[right]) === -1) {
                smaller = left
            } else {
                smaller = right
            }
            if(this.cmp(this.arr[smaller], this.arr[current]) === -1) {
                [this.arr[current], this.arr[smaller]] = [this.arr[smaller], this.arr[current]]
                current = smaller
            } else {
                break
            }
        }
    }
}