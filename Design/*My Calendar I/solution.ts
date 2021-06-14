class BTreeNode {
    left: BTreeNode
    right: BTreeNode
    start: number
    end: number
    
    constructor(start: number, end: number) {
        this.start = start;
        this.end = end;
    } 
}

class MyCalendar {
    root: BTreeNode
    constructor() {
        this.root = null
    }

    book(start: number, end: number): boolean {
        if(!this.root) {
            this.root = new BTreeNode(start, end)
            return true
        }
        let parent = null
        let current = this.root;
        while(true) {
            if(!current) {
                if(start >= parent.end) {
                    parent.right = new BTreeNode(start,end)
                    return true
                } else {
                    parent.left = new BTreeNode(start, end)
                    return true
                }
            }
            
            if(start >= current.end) {
                parent = current
                current = current.right
                continue;
            }
            
            if(end <= current.start) {
                parent = current
                current = current.left;
                continue
            }
            
            return false
        }
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */