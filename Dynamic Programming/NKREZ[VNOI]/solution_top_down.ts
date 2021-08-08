function maxTimes(intervals: number[][]) {
	let canAttendAt = new Map()
	for(let interval of intervals) {
		if(!canAttendAt.has(interval[0])) canAttendAt.set(interval[0], [])
		canAttendAt.get(interval[0]).push(interval)
	}
	let cache = new Map()
	function helper(currentTime: number) {
		if(currentTime > 30000) return 0
		const key = `${currentTime}`
		if(cache.has(key)) return cache.get(key)
		let result = Number.MIN_SAFE_INTEGER
		// Try joining each of this time event
		for(let canAttend of canAttendAt.get(currentTime)) {
			result = Math.max(result, canAttend[1] - canAttend[0] + helper(canAttend[1]))
		}
		// Not joining any of this time event
		result = Math.max(result, helper(currentTime + 1))
		cache.set(key, result)
		return result 
	}
	return helper(0)
}