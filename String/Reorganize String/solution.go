import "container/heap"

func reorganizeString(s string) string {
	result := ""
	MaxHeap := &Heap{}
	heap.Init(MaxHeap)
	freq := make(map[byte]int)
	for i := range s {
		freq[s[i]]++
	}
	for key, value := range freq {
		heap.Push(MaxHeap, []interface{}{key, value})
	}
	var previousLetter byte
	for MaxHeap.Len() > 0 {
		pop := heap.Pop(MaxHeap).([]interface{})
		if previousLetter == pop[0].(byte) {
			if MaxHeap.Len() == 0 {
				return ""
			} else {
				nextPop := heap.Pop(MaxHeap).([]interface{})
				result += string(nextPop[0].(byte))
				if nextPop[1].(int) != 1 {
					heap.Push(MaxHeap, []interface{}{nextPop[0], nextPop[1].(int) - 1})
				}
				previousLetter = nextPop[0].(byte)
				heap.Push(MaxHeap, pop)
			}
		} else {
			result += string(pop[0].(byte))
			if pop[1].(int) != 1 {
				heap.Push(MaxHeap, []interface{}{pop[0], pop[1].(int) - 1})
			}
			previousLetter = pop[0].(byte)
		}
	}
	return result
}

type Heap [][]interface{}

func (h Heap) Len() int           { return len(h) }
func (h Heap) Less(i, j int) bool { return h[i][1].(int) > h[j][1].(int) }
func (h Heap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *Heap) Push(x interface{}) {
	*h = append(*h, x.([]interface{}))
}

func (h *Heap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}