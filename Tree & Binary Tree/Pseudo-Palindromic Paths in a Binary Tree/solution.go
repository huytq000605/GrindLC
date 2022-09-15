/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pseudoPalindromicPaths (root *TreeNode) int {
    result := 0
    count := make([]int, 10, 10)
    var dfs func(node *TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        count[node.Val] += 1
        if node.Left == nil && node.Right == nil {
            count_odd := 0
            for i := 0; i < 10; i++ {
                if count[i] % 2 == 1 {
                    count_odd += 1
                }
            }
            if count_odd <= 1 {
                result += 1
            }
        }
        dfs(node.Left)
        dfs(node.Right)
        count[node.Val] -= 1
    }
    dfs(root)
    return result
}
