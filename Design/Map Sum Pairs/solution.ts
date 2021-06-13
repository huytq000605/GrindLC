class MapSum {
    map
    constructor() {
        this.map = new Map()
    }

    insert(key: string, val: number): void {
        this.map.set(key, val);
    }

    sum(prefix: string): number {
        let result = 0;
        for(let [key, value] of this.map.entries()) {
            if(key.startsWith(prefix)) result +=value
        }
        return result
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * var obj = new MapSum()
 * obj.insert(key,val)
 * var param_2 = obj.sum(prefix)
 */