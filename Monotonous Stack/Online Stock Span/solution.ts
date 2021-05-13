/*
This is a typical question using Monotonous Stack
The signal for this type of problem is counting something from previous like how many consecutive numbers greater/small than current number
*/

class StockSpanner {
    stack
    constructor() {
        this.stack = [];
    }

    next(price: number): number {
        let res = 1;
        while(this.stack.length && this.stack[this.stack.length - 1][0] <= price) {
            res += this.stack.pop()[1];
        }
        this.stack.push([price, res])
        return res;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */