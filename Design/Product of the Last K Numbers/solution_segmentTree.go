package main

type SegmentTree struct {
	Start   int
	End     int
	Product int
	Left    *SegmentTree
	Right   *SegmentTree
}

func (this *SegmentTree) Query(s, e int) int {
	if e < this.Start || s > this.End {
		return -1
	}

	if e >= this.End && s <= this.Start {
		return this.Product
	}

	this.normalize()
	leftQuery := this.Left.Query(s, e)
	rightQuery := this.Right.Query(s, e)
	if leftQuery == -1 {
		return rightQuery
	}
	if rightQuery == -1 {
		return leftQuery
	}
	return leftQuery * rightQuery
}

func (this *SegmentTree) Update(s, e, product int) {
	if e < this.Start || s > this.End {
		return
	}

	if e >= this.End && s <= this.Start {
		this.Product *= product
		return
	}

	this.normalize()
	this.Left.Update(s, e, product)
	this.Right.Update(s, e, product)

	this.Product = this.Left.Product * this.Right.Product
}

func (this *SegmentTree) normalize() {
	if this.Start != this.End {
		if this.Left == nil || this.Right == nil {
			middle := this.Start + (this.End-this.Start)/2
			this.Left = &SegmentTree{Start: this.Start, End: middle, Product: this.Product}
			this.Right = &SegmentTree{Start: middle + 1, End: this.End, Product: this.Product}
		}
	}
}

type ProductOfNumbers struct {
	root  *SegmentTree
	index int
}

func Constructor() ProductOfNumbers {
	return ProductOfNumbers{root: &SegmentTree{Start: 1, End: 40000, Product: 1}, index: 0}
}

func (this *ProductOfNumbers) Add(num int) {
	this.index++
	this.root.Update(this.index, this.index, num)
}

func (this *ProductOfNumbers) GetProduct(k int) int {
	return this.root.Query(this.index-k+1, this.index)
}
