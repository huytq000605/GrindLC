function maxTimes(intervals: number[][]) {
	let dp = new Array(30001).fill(0)
	let eventEndAt = new Map()
	for(let interval of intervals) {
		if(!eventEndAt.has(interval[1])) eventEndAt.set(interval[1], [])
		eventEndAt.get(interval[1]).push(interval)
	}
	for(let i = 1; i <= 30000; i++) {
		dp[i] = dp[i-1]
		if(eventEndAt.has(i)) {
			for(let interval of eventEndAt.get(i)) {
				dp[i] = Math.max(dp[i], dp[interval[0]] + interval[1] - interval[0]) 
			}
		}
	}
	return dp[30000]
}