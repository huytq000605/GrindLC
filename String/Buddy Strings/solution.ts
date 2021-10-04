function buddyStrings(s: string, goal: string): boolean {
    if(s.length !== goal.length) return false
    if(s === goal) {
        let set = new Set()
        for(let l of s) {
            if(set.has(l)) return true
            set.add(l)
        }
    }
    let count = 0
    let diff = -1
    for(let i = 0; i < s.length; i++) {
        if(s[i] !== goal[i]) {
            if(count === 0) diff = i
            else if(count === 1) {
                if(s[i] !== goal[diff] || s[diff] !== goal[i]) return false
            } else {
                return false
            }
            count++
        }
    }
    if(count === 0 || count === 1) return false
    return true
};