/**
 * Definition for node.
 * class Node {
 *     val: number
 *     children: Node[]
 *     constructor(val?: number) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = []
 *     }
 * }
 */

function levelOrder(root: Node | null,level = 0, result = []): number[][] {
    if(!root) return [];
    if(!result[level]) result[level] = [];
    result[level].push(root.val);
	for(let child of root.children) {
        levelOrder(child, level+1, result)
    }
    return result;
};
