package main

type StockSpanner struct {
	stack [][]int
}

func Constructor() StockSpanner {
	return StockSpanner{stack: [][]int{}}
}

func (this *StockSpanner) Next(price int) int {
	result := 1
	for len(this.stack) > 0 && this.stack[len(this.stack)-1][1] <= price {
		result += this.stack[len(this.stack)-1][0]
		this.stack = this.stack[:len(this.stack)-1]
	}
	this.stack = append(this.stack, []int{result, price})
	return result
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
