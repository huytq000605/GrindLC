import {readline, print, testOutput} from "@ip-algorithmics/codeforces-io"
import fs from "fs"

let numberOfTests = parseInt(readline(), 10)

for(let i = 0; i < numberOfTests; i++) {
    let str = readline().trim()
    let graphLines = readline().trim()
    let swaps = []
    for(let i = 0; i < Number(graphLines); i++) {
        swaps.push(readline())
    }
    
    print(`Case #${i+1}: ${solve(str, swaps)}`)
    fs.appendFileSync("output.txt", `Case #${i+1}: ${solve(str, swaps)}` + "\n")
}
testOutput()


function solve(str: string, swaps: string[]) {
    let graph = Array(26).fill(0).map(() => Array(26).fill(Number.MAX_SAFE_INTEGER))
    for(let i = 0; i < 26; i++) {
        graph[i][i] = 0
    }
    for(let swap of swaps) {
        let src = swap[0].charCodeAt(0) - "A".charCodeAt(0)
        let dest = swap[1].charCodeAt(0) - "A".charCodeAt(0)
        graph[src][dest] = 1
    }
    for(let src = 0; src < 26; src++) {
        let queue = []
        for(let dest = 0; dest < 26; dest++) {
            if(src === dest) continue
            if(graph[src][dest] < Number.MAX_SAFE_INTEGER) {
                queue.push([dest, 1])
            }
        }
        while(queue.length) {
            let [current, distance] = queue.shift()
            for(let newDest = 0; newDest < 26; newDest++) {
                let newDistance = distance + graph[current][newDest]
                if(newDistance < graph[src][newDest]) {
                    graph[src][newDest] = newDistance
                    queue.push([newDest, newDistance])
                } 
            }
        }
    }
    let result = -1
    for(let i = 0; i < 26; i++) {
        let res = 0
        for(let l of str) {
            let src = l.charCodeAt(0) - "A".charCodeAt(0)
            if(graph[src][i] === Number.MAX_SAFE_INTEGER) {
                res = -1
                break
            } else {
                res += graph[src][i]
            }
        }
        if(result === -1) {
            result = res
        } else if(res !== -1) {
            result = Math.min(result, res)
        }
    }
    
    return result
}
