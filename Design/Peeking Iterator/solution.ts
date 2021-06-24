/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Iterator {
 *      hasNext(): boolean {}
 *
 *      next(): number {}
 * }
 */

 class PeekingIterator {
    iterator
    cache
    constructor(iterator: Iterator) {
        this.iterator = iterator
        this.cache = null
    }

    peek(): number {
        if(this.cache) return this.cache
        this.cache = this.iterator.next()
        return this.cache
    }

    next(): number {
        if(this.cache) {
            const result = this.cache
            this.cache = null
            return result
        }
        return this.iterator.next()
    }

    hasNext(): boolean {
        if(this.cache) return true
        return this.iterator.hasNext()
    }
}

/**
 * Your PeekingIterator object will be instantiated and called as such:
 * var obj = new PeekingIterator(iterator)
 * var param_1 = obj.peek()
 * var param_2 = obj.next()
 * var param_3 = obj.hasNext()
 */