function findLatestStep(arr: number[], m: number): number {
    let union = new UnionFind(arr.length)
    let visited = Array(arr.length + 2).fill(0)
    let result = -1
    for(let i = 0; i < arr.length; i++) {
        visited[arr[i]] = 1
        union.groupLength[arr[i]] = 1
        union.length[1]++
        if(visited[arr[i] + 1] === 1) {
            union.union(arr[i], arr[i] + 1)
        }
        if(visited[arr[i] - 1] === 1) {
            union.union(arr[i], arr[i] - 1)
        }
        if(union.length[m] > 0) result = i+1
    }
    return result
};

class UnionFind {
    parent
    length
    rank
    groupLength
    
    constructor(n) {
        this.parent = Array(n + 1).fill(0).map((e, i) => i)
        this.rank = Array(n + 1).fill(0)
        this.length = Array(n + 1).fill(0)
        this.groupLength = Array(n + 1).fill(0)
        
    }
    
    find(x) {
        if(this.parent[x] !== x) {
            return this.find(this.parent[x])
        } else {
            return x
        }
    }
    
    union(x, y) {
        let setX = this.find(x)
        let setY = this.find(y)
        if(setX === setY) {
            return setX
        }
        let newLength = this.groupLength[setX] + this.groupLength[setY]
        this.length[newLength]++
        this.length[this.groupLength[setX]]--
        this.length[this.groupLength[setY]]--
        this.groupLength[setX] = newLength
        this.groupLength[setY] = newLength
        
        if(this.rank[setX] === this.rank[setY]) {
            this.rank[setX]++
            this.parent[setY] = setX
            return setX
        }
        if(this.rank[setX] < this.rank[setY]) {
            this.parent[setX] = setY
            return setY
        } else {
            this.parent[setY] = setX
            return setX
        }
    }
    
}