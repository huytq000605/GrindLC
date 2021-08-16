function numberOfSets(n: number, k: number): number {
    let cache = Array(n).fill(0).map(() => Array(k))
    let helper = (start: number, k: number) => {
        if(k === 0) return 1 
        if(cache[start][k] !== undefined) return cache[start][k]
        let result = 0
        for(let newStart = start + 1; newStart < n; newStart++) {
            if((n - 1 - newStart) < k - 1) break // If we cannot go this far (dont have enough points to make enough segments)
            let waysToDo = newStart - start // When we choose new start, we have (newStart - start) ways to make the segment end at newStart
            result += (helper(newStart, k-1) * waysToDo) % (1e9 + 7)
            result = result % (1e9 + 7)
        }
        
        cache[start][k] = result
        return result
    }
    return helper(0, k)
};