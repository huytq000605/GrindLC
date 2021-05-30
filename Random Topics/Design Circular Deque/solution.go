package main

type MyCircularDeque struct {
	arr    []int
	length int
}

/** Initialize your data structure here. Set the size of the deque to be k. */
func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{
		arr:    make([]int, 0),
		length: k,
	}
}

/** Adds an item at the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertFront(value int) bool {
	if this.length == len(this.arr) {
		return false
	} else {
		res := []int{value}
		res = append(res, this.arr...)
		this.arr = res
		return true
	}
}

/** Adds an item at the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertLast(value int) bool {
	if this.length == len(this.arr) {
		return false
	} else {
		this.arr = append(this.arr, value)
		return true
	}
}

/** Deletes an item from the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteFront() bool {
	if len(this.arr) > 0 {
		this.arr = this.arr[1:]
		return true
	} else {
		return false
	}

}

/** Deletes an item from the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteLast() bool {
	if len(this.arr) > 0 {
		this.arr = this.arr[:len(this.arr)-1]
		return true
	} else {
		return false
	}
}

/** Get the front item from the deque. */
func (this *MyCircularDeque) GetFront() int {
	if len(this.arr) > 0 {
		return this.arr[0]
	} else {
		return -1
	}
}

/** Get the last item from the deque. */
func (this *MyCircularDeque) GetRear() int {
	if len(this.arr) > 0 {
		return this.arr[len(this.arr)-1]
	} else {
		return -1
	}
}

/** Checks whether the circular deque is empty or not. */
func (this *MyCircularDeque) IsEmpty() bool {
	if len(this.arr) > 0 {
		return false
	} else {
		return true
	}
}

/** Checks whether the circular deque is full or not. */
func (this *MyCircularDeque) IsFull() bool {
	if len(this.arr) == this.length {
		return true
	} else {
		return false
	}
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */
