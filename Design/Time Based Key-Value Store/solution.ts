class TimeMap {
    map: Map<string, string>
    keyTimeMapping: Map<string, number[]>
    constructor() {
        this.map = new Map()
        this.keyTimeMapping = new Map()
    }

    set(key: string, value: string, timestamp: number): void {
        let keyMap = `${key}-${timestamp}`
        this.map.set(keyMap, value)
        if(!this.keyTimeMapping.get(key)) {
            this.keyTimeMapping.set(key, [])
        }
        this.keyTimeMapping.get(key).push(timestamp)
    }

    get(key: string, timestamp: number): string {
        let arr = this.keyTimeMapping.get(key)
        for(let i = arr.length - 1; i >= 0; i--) {
            if(arr[i] > timestamp) continue
            if(arr[i] <= timestamp) {
                let keyMap = `${key}-${arr[i]}`
                return this.map.get(keyMap)
            }
        }
        return ""
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */