class LRUCache {
    head: DLLNode
    tail: DLLNode
    map: Map<number, DLLNode>
    capacity: number
    constructor(capacity: number) {
        this.capacity = capacity
        this.head = new DLLNode(null, 0)
        this.tail = new DLLNode(null, 0)
        this.head.next = this.tail
        this.tail.prev = this.head
        this.map = new Map()
    }

    get(key: number): number {
        if(this.map.has(key)) {
            let value = this.map.get(key).val
            this.deleteNode(this.map.get(key))
            this.put(key, value)
            return value
        } else {
            return -1
        }
    }

    put(key: number, value: number): void {
        if(this.map.has(key)) this.deleteNode(this.map.get(key))
        else if(this.map.size === this.capacity) {
            this.deleteNode(this.head.next)
        }
        let tail = this.tail.prev
        let newNode = new DLLNode(key, value)
        this.map.set(key, newNode)
        tail.next = newNode
        newNode.prev = tail
        newNode.next = this.tail
        this.tail.prev = newNode
    }

    private deleteNode(node) {
        this.map.delete(node.key)
        let next = node.next
        let prev = node.prev
        if(next) next.prev = prev
        if(prev) prev.next = next
    }
}

class DLLNode {
    key: number
    val: number
    prev: DLLNode
    next: DLLNode
    
    constructor(key: number, val: number) {
        this.key = key
        this.val = val
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */