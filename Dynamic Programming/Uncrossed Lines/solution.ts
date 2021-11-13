function maxUncrossedLines(nums1: number[], nums2: number[]): number {
    let dp = Array(nums1.length).fill(0).map(() => Array(nums2.length))
    let dfs = (idx1: number, idx2: number) => {
        if(idx1 >= nums1.length || idx2 >= nums2.length) return 0
        if(dp[idx1][idx2] !== undefined) return dp[idx1][idx2]
        if(nums1[idx1] === nums2[idx2]) {
            dp[idx1][idx2] = dfs(idx1 + 1, idx2 + 1) + 1
        } else {
            dp[idx1][idx2] = Math.max(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1))
        }
        return dp[idx1][idx2]
    }
    return dfs(0, 0)
};