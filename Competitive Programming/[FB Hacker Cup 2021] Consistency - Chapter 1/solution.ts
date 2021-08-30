import {readline, print, testOutput} from "@ip-algorithmics/codeforces-io"
import fs from "fs";

let numberOfLines = parseInt(readline(), 10);
for(let i = 0; i < numberOfLines; i++) {
    let x = readline().trim()
    print(solve(x))
    fs.appendFileSync("output.txt", `Case #${i+1}: ${solve(x)}` + "\n")
}
testOutput()


function solve(str: string) {
    let vowels = 0
    let consonants = 0
    let freq = Array(26).fill(0)
    for(let l of str) {
        if(l === "U" || l === "E" || l === "O" || l === "A" || l === "I") {
            vowels++
        } else {
            consonants++
        }
        freq[l.charCodeAt(0) - "A".charCodeAt(0)]++
    }
    let result = Number.MAX_SAFE_INTEGER
    for(let choose = 0; choose < 26; choose++) {
        if(choose === 20 || choose === 14 || choose === 0 || choose === 4 || choose === 8) {
            result = Math.min(result, consonants + (vowels - freq[choose]) * 2)
        } else {
            result = Math.min(result, vowels + (consonants - freq[choose]) * 2)   
        }
    }
    return result
}