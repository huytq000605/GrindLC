class LLNode {
    prev: LLNode;
    next: LLNode;
    val: number;
    key: number;
    constructor(key: number, val: number) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    head: LLNode;
    tail: LLNode;
    capacity: number;
    length: number;
    map: Map<number, LLNode>;
    constructor(capacity: number) {
        this.capacity = capacity;
        this.length = 0;
        this.head = null;
        this.tail = null;
        this.map = new Map();
    }

    get(key: number): number {
        if (!this.map.has(key)) {
            return -1;
        }
        let node = this.map.get(key);
        let result = node.val;
        if (this.tail === node) {
            return result;
        }
        if (this.head === node && node.next) {
            this.head = node.next;
        }
        if (node.prev) {
            node.prev.next = node.next;
        }
        if (node.next) {
            node.next.prev = node.prev;
        }
        this.tail.next = node;
        node.prev = this.tail;
        this.tail = node;
        return result;
    }

    put(key: number, value: number): void {
        let node = null;
        if (this.map.has(key)) {
            node = this.map.get(key);
            if (this.head === node && node.next) {
                this.head = node.next;
            }
            node.val = value;
            if (this.tail === node) {
                return;
            }
            if (node.prev) {
                node.prev.next = node.next;
            }
            if (node.next) {
                node.next.prev = node.prev;
            }
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        } else {
            if (this.length === this.capacity) {
                this.map.delete(this.head.key);
                this.head = this.head.next;
                if (this.head) this.head.prev = null;
                this.length--;
            }
            node = new LLNode(key, value);
            if (this.length === 0) {
                this.head = node;
                this.tail = node;
            } else {
                this.tail.next = node;
                node.prev = this.tail;
                this.tail = node;
            }
            if (this.length !== this.capacity) this.length++;
            this.map.set(key, node);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
