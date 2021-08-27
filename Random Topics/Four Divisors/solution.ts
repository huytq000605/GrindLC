function sumFourDivisors(nums: number[]): number {
    let result = 0
    let cache = new Map()
    function cal(num) {
        if(cache.has(num)) return cache.get(num)
        let sum = 0
        let count = 0
        for(let i = 1; i <= Math.sqrt(num); i++) {
            if(i === Math.sqrt(num)) {
                sum += i
                count++
            } else if(num % i === 0) {
                sum += i
                sum += num / i
                count+=2
            }
            if(count > 4) {
                cache.set(num, 0)
                return 0
            }
        }
        if(count !== 4) {
            cache.set(num, 0)
            return 0
        }
        cache.set(num, sum)
        return sum
    }
    
    for(let num of nums) {
        result += cal(num)
    }
    return result
    
    
};

