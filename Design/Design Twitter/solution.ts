class Twitter {
    tweet
    followMap
    time
    constructor() {
        this.tweet = new Map()
        this.followMap = new Map()
        this.time = 0
    }

    postTweet(userId: number, tweetId: number): void {
        if(!this.tweet.has(userId)) this.tweet.set(userId, [])
        this.tweet.get(userId).push([tweetId, this.time++])
    }

    getNewsFeed(userId: number): number[] {
        let minHeap = new MaxHeap<any>((a,b) => {
            if(a[1] < b[1]) return -1
            if(a[1] > b[1]) return 1
        })

        let arrays = [] // K sorted arrays

        if(this.tweet.has(userId)) {
            let array = this.tweet.get(userId)
            let idx = arrays.length
            arrays.push(array)
            minHeap.push([...array[array.length - 1], idx, array.length - 1])
        }

        if(this.followMap.has(userId)) {
            for(let follow of this.followMap.get(userId).values()) {
                if(this.tweet.has(follow)) {
                    let array = this.tweet.get(follow)
                    let idx = arrays.length
                    arrays.push(array)
                    minHeap.push([...array[array.length - 1], idx, array.length - 1])
                }
            }
        }
        
        let result = [] // Merge K sorted arrays into 1 array with max length = 10
        while(minHeap.length && result.length < 10) {
            let [tweetId, time, arrayIdx, currentIdxOfArray] = minHeap.pop()
            result.push(tweetId)
            if(currentIdxOfArray > 0) {
                currentIdxOfArray--
                minHeap.push([...arrays[arrayIdx][currentIdxOfArray], arrayIdx, currentIdxOfArray])
            }
        }
        
        return result
        
    }

    follow(followerId: number, followeeId: number): void {
        if(!this.followMap.has(followerId)) this.followMap.set(followerId, new Set())
        this.followMap.get(followerId).add(followeeId)
    }

    unfollow(followerId: number, followeeId: number): void {
        if(this.followMap.has(followerId)) {
            this.followMap.get(followerId).delete(followeeId)
        }
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * var obj = new Twitter()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */
 class MaxHeap<T> {
    private heap: T[];
    private compare: (node1: T, node2: T) => 1 | -1 | 0;
    /**
     *
     * @param compareFunction return 1 if node 1 > node 2, return -1 if node 1 < node 2, return 0 if node1 = node2
     */
    constructor(compareFn: (node1: T, node2: T) => 1 | -1 | 0) {
        this.heap = [];
        this.compare = compareFn;
    }

    get length(): number {
        return this.heap.length;
    }

    public peek(): T | undefined {
        if (this.length > 0) return this.heap[0];
        else return undefined;
    }

    public push(node: T): void {
        this.heap.push(node);
        this.bubbleUp();
    }

    public pop(): T | undefined {
        if (this.length === 0) {
            return undefined;
        }
        [this.heap[0], this.heap[this.length - 1]] = [
            this.heap[this.length - 1],
            this.heap[0],
        ];
        const pop = this.heap.pop();
        this.bubbleDown();
        return pop;
    }

    private bubbleUp(): void {
        let current = this.length - 1;
        while (current > 0) {
            let parent = Math.ceil(current / 2) - 1;
            if (this.compare(this.heap[current], this.heap[parent]) == 1) {
                [this.heap[current], this.heap[parent]] = [
                    this.heap[parent],
                    this.heap[current],
                ];
                current = parent;
            } else {
                return;
            }
        }
    }

    private bubbleDown(): void {
        let current = 0;
        while (true) {
            let left = current * 2 + 1;
            if (left >= this.length) return;
            let right = left + 1;
            if (right >= this.length) right = left;
            let bigger: number;
            if (this.compare(this.heap[left], this.heap[right]) == 1) {
                bigger = left;
            } else {
                bigger = right;
            }
            if (this.compare(this.heap[bigger], this.heap[current]) == 1) {
                [this.heap[bigger], this.heap[current]] = [
                    this.heap[current],
                    this.heap[bigger],
                ];
                current = bigger;
            } else {
                return;
            }
        }
    }
}
