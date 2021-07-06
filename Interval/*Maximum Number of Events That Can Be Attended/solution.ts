function maxEvents(events: number[][]): number {
    let result = 0;
    let currentDay = 0;
    events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    let eventNum = 0;
    let heap = new MinHeap();
    while (currentDay <= 100000) {
        if (heap.isEmpty()) { // Skip the day do nothing ( for optimized )
            if (eventNum < events.length) {
                currentDay = events[eventNum][0];
            } else {
                break;
            }
        }

        while (eventNum < events.length && events[eventNum][0] <= currentDay) { // Insert all events are happening
            heap.insert(events[eventNum]);
            eventNum++;
        }

        while (!heap.isEmpty() && heap.peek()[1] < currentDay) { // Remove all events have ended 
            heap.pop();
        }

        if (!heap.isEmpty()) { // Attend the top event from the heap and go to next day
            heap.pop();
            result++;
        }

        currentDay++;
    }
    return result;
}

class MinHeap {
    arr: number[];
    constructor() {
        this.arr = [];
    }

    insert(event) {
        this.arr.push(event);
        this.bubbleUp();
    }

    pop() {
        [this.arr[0], this.arr[this.arr.length - 1]] = [
            this.arr[this.arr.length - 1],
            this.arr[0],
        ];
        const pop = this.arr.pop();
        this.bubbleDown();
        return pop;
    }

    peek() {
        return this.arr[0];
    }

    isEmpty() {
        if (this.arr.length == 0) {
            return true;
        }
        return false;
    }

    bubbleUp() {
        let current = this.arr.length - 1;
        while (current > 0) {
            let parent = Math.floor((current - 1) / 2);
            if (this.arr[current][1] < this.arr[parent][1]) {
                [this.arr[current], this.arr[parent]] = [
                    this.arr[parent],
                    this.arr[current],
                ];
            }
            current = parent;
        }
    }

    bubbleDown() {
        let current = 0;
        while (current <= this.arr.length - 1) {
            let left = current * 2 + 1;
            let right = current * 2 + 2;
            if (left > this.arr.length - 1) {
                return;
            }
            if (right > this.arr.length - 1) {
                right = left;
            }
            let compare = this.arr[left][1] < this.arr[right][1] ? left : right;
            if (this.arr[current][1] > this.arr[compare][1]) {
                [this.arr[current], this.arr[compare]] = [
                    this.arr[compare],
                    this.arr[current],
                ];
            }
            current = compare;
        }
    }
}