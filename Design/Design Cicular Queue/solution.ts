class LL {
    val
    next
    prev
    constructor(val) {
        this.val = val
    }
}

class MyCircularQueue {
    length
    capacity
    head
    tail
    constructor(k: number) {
        this.capacity = k
        this.length = 0
        this.head = new LL(0)
        this.tail = new LL(0)
        this.head.next = this.tail
        this.tail.prev = this.head
    }

    enQueue(value: number): boolean {
        if(this.length < this.capacity) {
            this.length++
            let prevTail = this.tail.prev
            let newNode = new LL(value)
            prevTail.next = newNode
            newNode.prev = prevTail
            newNode.next = this.tail
            this.tail.prev = newNode
            return true
        } else {
            return false
        }
    }


    deQueue(): boolean {
        if(this.length > 0) {
            this.length--
            let nextFirst = this.head.next.next
            nextFirst.prev = this.head
            this.head.next = nextFirst
            return true
        } else {
            return false
        }
    }

    Front(): number {
        if(!this.length) return -1
        return this.head.next.val
    }

    Rear(): number {
        if(!this.length) return -1
        return this.tail.prev.val
    }

    isEmpty(): boolean {
        return this.length === 0
    }

    isFull(): boolean {
        return this.length === this.capacity
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */