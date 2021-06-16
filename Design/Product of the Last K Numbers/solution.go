package main

type ProductOfNumbers struct {
	prefixSum []int
}

func Constructor() ProductOfNumbers {
	return ProductOfNumbers{prefixSum: []int{1}}
}

func (this *ProductOfNumbers) Add(num int) {
	if num > 0 {
		this.prefixSum = append(this.prefixSum, this.prefixSum[len(this.prefixSum)-1]*num)
	} else {
		this.prefixSum = []int{1}
	}
}

func (this *ProductOfNumbers) GetProduct(k int) int {
	if k > len(this.prefixSum)-1 { // We add a fake element 1
		return 0
	}
	last := len(this.prefixSum) - 1
	return this.prefixSum[last] / this.prefixSum[last-k]
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(num);
 * param_2 := obj.GetProduct(k);
 */
