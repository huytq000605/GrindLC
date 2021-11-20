class RandomizedSet {
    arr
    map
    constructor() {
        this.map = new Map()
        this.arr = []
    }

    insert(val: number): boolean {
        if(this.map.has(val)) return false
        this.arr.push(val)
        this.map.set(val, this.arr.length - 1)
        return true
    }

    remove(val: number): boolean {
        if(!this.map.has(val)) return false
        let currentIdx = this.map.get(val)
        
        this.map.set(this.arr[this.arr.length - 1], currentIdx);
        this.arr[currentIdx] = this.arr[this.arr.length - 1]
        this.arr.pop()
        this.map.delete(val)
        
        return true
        
    }

    getRandom(): number {
        let rand = Math.floor(Math.random() * this.arr.length)
        return this.arr[rand]
        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */