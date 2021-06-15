package main

type MinHeap struct {
	arr []int
}

func (this *MinHeap) Insert(val int) {
	this.arr = append(this.arr, val)
	this.bubbleUp()
	return
}

func (this *MinHeap) Pop() int {
	pop := this.arr[0]
	this.arr[len(this.arr)-1], this.arr[0] = this.arr[0], this.arr[len(this.arr)-1]
	this.arr = this.arr[:len(this.arr)-1]
	this.bubbleDown()
	return pop
}

func (this *MinHeap) bubbleDown() {
	current := 0
	for current <= len(this.arr)-1 {
		leftChild := current*2 + 1
		if leftChild > len(this.arr)-1 {
			return
		}
		rightChild := current*2 + 2
		if rightChild > len(this.arr)-1 {
			if this.arr[current] > this.arr[leftChild] {
				this.arr[current], this.arr[leftChild] = this.arr[leftChild], this.arr[current]
				current = leftChild
				continue
			}
			return
		}
		compare := 0
		if this.arr[leftChild] < this.arr[rightChild] {
			compare = leftChild
		} else {
			compare = rightChild
		}
		if this.arr[current] > this.arr[compare] {
			this.arr[current], this.arr[compare] = this.arr[compare], this.arr[current]
			current = compare
		} else {
			return
		}
	}
}

func (this *MinHeap) bubbleUp() {
	current := len(this.arr) - 1
	for current > 0 {
		parent := (current - 1) / 2
		if this.arr[current] < this.arr[parent] {
			this.arr[current], this.arr[parent] = this.arr[parent], this.arr[current]
			current = parent
		} else {
			return
		}
	}
}

type SeatManager struct {
	Heap MinHeap
}

func Constructor(n int) SeatManager {
	seatManager := SeatManager{Heap: MinHeap{arr: []int{}}}
	for i := 1; i <= n; i++ {
		seatManager.Heap.Insert(i)
	}
	return seatManager
}

func (this *SeatManager) Reserve() int {
	return this.Heap.Pop()
}

func (this *SeatManager) Unreserve(seatNumber int) {
	this.Heap.Insert(seatNumber)
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Reserve();
 * obj.Unreserve(seatNumber);
 */
