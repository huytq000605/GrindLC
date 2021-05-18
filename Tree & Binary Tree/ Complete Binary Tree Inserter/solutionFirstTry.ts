// Definition for a binary tree node.
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
    root;
    currentMaxLevel
    constructor(root: TreeNode | null) {
        this.root = root;
        this.setMaxLevel(this.root, 0);
        return this
    }

    insert(v: number): number {
        this.setMaxLevel(this.root, 0)
        const node = this.getNode(this.root, 0);
        if(!node.left) node.left = new TreeNode(v);
        else node.right = new TreeNode(v);
        return node.val;
    }

    get_root(): TreeNode | null {
        return this.root
    }

    private setMaxLevel(node, level) {
        if(!node) return null
        if(!node.left || !node.right) {
            this.currentMaxLevel = level;
            return level;
        }
        let leftLevel = this.setMaxLevel(node.left, level + 1) || level
        let rightLevel = this.setMaxLevel(node.right, level + 1) || level
        this.currentMaxLevel = Math.min(leftLevel, rightLevel);
        return this.currentMaxLevel
    }

    private getNode(node, level) {
        if(!node) return null
        if(level > this.currentMaxLevel) return null
        if(level == this.currentMaxLevel) {
            if(!node.left || !node.right) return node;
        }
        let left = this.getNode(node.left, level + 1);
        if(left) return left
        return this.getNode(node.right, level + 1);
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * var obj = new CBTInserter(root)
 * var param_1 = obj.insert(v)
 * var param_2 = obj.get_root()
 */