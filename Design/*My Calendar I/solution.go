package main

type node struct {
	Start int
	End   int
	Left  *node
	Right *node
}

type MyCalendar struct {
	Root *node
}

func Constructor() MyCalendar {
	return MyCalendar{}
}

func (this *MyCalendar) Insert(start int, end int, current **node) bool {
	if (*current) == nil {
		*current = &node{
			Start: start,
			End:   end,
		}
		return true
	}
	if start >= (*current).End {
		return this.Insert(start, end, &(*current).Right)
	}
	if end <= (*current).Start {
		return this.Insert(start, end, &(*current).Left)
	}
	return false
}

func (this *MyCalendar) Book(start int, end int) bool {
	return this.Insert(start, end, &this.Root)
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
