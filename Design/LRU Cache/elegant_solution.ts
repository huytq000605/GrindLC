class LRUCache {
    private count = 0
    private orderedMap = new Map()
    private capacity
    constructor(capacity: number) {
        this.capacity = capacity
    }

    get(key: number): number {
        if(!this.orderedMap.has(key)) {
            return -1
        }
        let result = this.orderedMap.get(key)
        this.orderedMap.delete(key)
        this.orderedMap.set(key, result)
        return result
    }

    put(key: number, value: number): void {
        if(!this.orderedMap.has(key)) {
            this.orderedMap.set(key, value)
            this.count++
            if(this.count > this.capacity) {
                let lru = this.orderedMap.keys().next().value
                this.orderedMap.delete(lru)
                this.count--
            }
        } else {
            this.orderedMap.delete(key)
            this.orderedMap.set(key,value)
        }
        
    }
}
