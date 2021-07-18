function maxPoints(points: number[][]): number {
    let prevRow = Array(points[0].length)
    for(let col = 0; col < points[0].length; col++) {
            prevRow[col] = points[0][col]
    }
	// For each row, to avoid TLE, we use another DP technique is that, we calculate the maximum value from left and from right, the final maximum value for it is maximum of from left and from right	
	// left[i] is maximum previous value to build current[i] if takes only index from 0 to i
	// right[i] is maximum previous value to build current[i] if takes only index from i to points[0].length
    for(let row = 1; row < points.length; row++) {
        let currentRow = Array(points[0].length).fill(0)
        let left = Array(points[0].length).fill(0)
        let right = Array(points[0].length).fill(0)
        left[0] = prevRow[0]
        for(let i = 1; i < points[0].length; i++) {
            left[i] = Math.max(left[i - 1] - 1, prevRow[i])
        }
        right[points[0].length - 1] = prevRow[points[0].length - 1]
        for(let i = points[0].length - 2; i >= 0; i--) {
            right[i] = Math.max(right[i+1] - 1, prevRow[i])
        }
        for(let i = 0; i < currentRow.length; i++) {
            currentRow[i] = points[row][i] + Math.max(left[i], right[i])
        }
        prevRow = currentRow
    }
    return Math.max(...prevRow)
};