function loudAndRich(richer: number[][], quiet: number[]): number[] {
    let richerMap = new Map()
    for(let i = 0; i < quiet.length; i++) {
        richerMap.set(i, [])
    }

    for(let rich of richer) {
        richerMap.get(rich[1]).push(rich[0])
    }

    let result = Array(quiet.length)
    for(let i = 0; i < quiet.length; i++) {
        result[i] = i
    }

    function dfs(currentPerson: number, seen: Map<number, number>): number {
        if(seen.has(currentPerson)) {
            return seen.get(currentPerson)
        }
        result[currentPerson] = currentPerson
        
        for(let richerPerson of richerMap.get(currentPerson)) {
            if(quiet[dfs(richerPerson, seen)] < quiet[result[currentPerson]]) {
                result[currentPerson] = result[dfs(richerPerson, seen)]
            }
                
        }
        seen.set(currentPerson, result[currentPerson])
        return result[currentPerson]
    }

    let seen = new Map()
    for(let i = 0; i < quiet.length; i++) {
        result[i] = dfs(i, seen)
    }
    return result
};


