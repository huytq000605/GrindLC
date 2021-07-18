function wordBreak(s: string, wordDict: string[]): string[] {
    let map = new Map()
    for(let w of wordDict) {
        map.set(w, true)
    }
    let cache = new Map()
    function helper(str: string): string[] {
        if(str === "") return [""]
        if(cache.has(str)) return cache.get(str)
        let result = []
        for(let i = 0; i < str.length; i++) {
            let start = str.slice(0, i + 1)
            if(map.has(start)) {
                let res = helper(str.slice(i + 1))
                for(let r of res) {
                    if(r === "") result.push(start)
                    else result.push(start + " " + r)
                }
            }
        }
        cache.set(str, result)
        return result
    }
    return helper(s)
};