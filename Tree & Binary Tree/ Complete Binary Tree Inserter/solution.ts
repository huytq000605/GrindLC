class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

class CBTInserter {
    root: TreeNode | null;
    queue: TreeNode[] = []

    constructor(root: TreeNode | null) {
        this.root = root;
        this.queue.push(this.root);
        while(true) {
            let current = this.queue[0];
            if(current.left && current.right) {
                this.queue.push(current.left);
                this.queue.push(current.right);
                this.queue.shift();
            }
            else {
                break;
            }
        }
    }

    insert(v: number): number {
        let current = this.queue[0];
        if(!current.left) {
            current.left = new TreeNode(v);
        } else {
            current.right = new TreeNode(v)
            this.queue.push(current.left)
            this.queue.push(current.right);
            this.queue.shift();
        }
        return current.val;
    }

    get_root(): TreeNode | null {
        return this.root;
    }
}