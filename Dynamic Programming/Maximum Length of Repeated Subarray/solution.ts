// This problem doesn't accept top down approach on leetcode ( TLE )

function findLength(nums1: number[], nums2: number[]): number {
    let cache = new Map()
    function helper(start1, start2, starting = true) {
        const key = `${start1}-${start2}-${starting}`
        if(cache.has(key)) {
            return cache.get(key)
        }
        if(start1 === nums1.length || start2 === nums2.length) {
            return 0
        }
        if(starting === false) {
            if(nums1[start1] === nums2[start2]) {
                cache.set(key, 1 + helper(start1 + 1, start2+ 1, false))
                return cache.get(key)
            } else {
                return 0
            }
        } else {
            let res1 = 0, res2 = 0, res3 = 0;
            if(nums1[start1] === nums2[start2]) {
                res1 = 1 + helper(start1 + 1, start2 + 1, false)
            }
            res2 = helper(start1 + 1, start2, true)
            res3 = helper(start1, start2 + 1, true)
            cache.set(key, Math.max(res1, res2, res3))
            return cache.get(key)
        }
    }
    return helper(0, 0, true)
};

