/*
Dfs for every key in equal map, if in dfs function, have notEqual then it's conflicted
*/
function equationsPossible(equations: string[]): boolean {
    let equal = new Map()
    let notEqual = new Map()
    for(let equation of equations) {
        equal.set(equation[0], equal.get(equation[0]) || [])
        equal.set(equation[3], equal.get(equation[3]) || [])
        notEqual.set(equation[0], notEqual.get(equation[0]) || new Map())
        notEqual.set(equation[3], notEqual.get(equation[3]) || new Map())
        if(equation[1] === "=") {
            equal.get(equation[0]).push(equation[3])
            equal.get(equation[3]).push(equation[0])
        } else {
            notEqual.get(equation[0]).set(equation[3], true)
            notEqual.get(equation[3]).set(equation[0], true)
        }
    }
    for(let key of equal.keys()) {
        if(dfs(equal, notEqual, new Set(), key, key) === false) return false
    }
    return true
    
};

function dfs(equal: Map<string, string[]>, notEqual: Map<string, Set<string>>, seen: Set<string>, src: string, dest: string) {
    if(notEqual.has(src) && notEqual.get(src).has(dest)) return false
    seen.add(dest)
    for(let connected of equal.get(dest)) {
        if(seen.has(connected)) {
            continue
        }
        if(dfs(equal, notEqual, seen, src, connected) === false) return false
        
    }
    return true
}