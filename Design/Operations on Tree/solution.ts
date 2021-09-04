class LockingTree {
    parent: number[]
    child: Map<number, number[]>
    lockMap: Map<number, number>
    constructor(parent: number[]) {
        this.parent = parent
        this.child = new Map()
        this.lockMap = new Map()
        for(let i = 0; i < parent.length; i++) {
            if(parent[i] === -1) continue
            if(!this.child.has(parent[i])) this.child.set(parent[i], [])
            this.child.get(parent[i]).push(i)
        }
    }

    lock(num: number, user: number): boolean {
        if(!this.lockMap.has(num)) {
            this.lockMap.set(num, user)
            return true
        }
        return false
    }

    unlock(num: number, user: number): boolean {
        if(!this.lockMap.has(num)) {
            return false
        }
        if(this.lockMap.get(num) !== user) return false
        this.lockMap.delete(num)
        return true
    }

    upgrade(num: number, user: number): boolean {
        let dfsParent = (current) => {
            if(this.lockMap.has(current)) return false
            if(this.parent[current] === -1) return true
            return dfsParent(this.parent[current])
        }
        if(!dfsParent(num)) return false
        let flag = false
        let dfsChild = (current) => {
            if(current !== num) {
                if(this.lockMap.has(current)) {
                    flag = true
                    this.lockMap.delete(current)
                }
            }
            if(this.child.has(current)) {
                for(let child of this.child.get(current)) {
                    dfsChild(child)
                }
            }
        }
        dfsChild(num)
        if(flag) this.lock(num, user)
        return flag
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * var obj = new LockingTree(parent)
 * var param_1 = obj.lock(num,user)
 * var param_2 = obj.unlock(num,user)
 * var param_3 = obj.upgrade(num,user)
 */