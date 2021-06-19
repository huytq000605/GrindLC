/*
By observe, we can know no matters where the "0" are, we can push all of it to the left but dont touch the leading "1", the rest will all be 1,
all 0 can transform to 1 except the last one => result
*/

function maximumBinaryString(binary: string): string {
    let zeroCount = 0
    let firstOnes = 0
    for(let i = 0; i < binary.length; i++) {
        if(binary[i] === "0") {
            zeroCount++
        } else if (zeroCount === 0) {
            firstOnes++
        }
    }
    if(zeroCount == 0) return binary
    return Array(firstOnes).fill("1").join("") + Array(zeroCount - 1).fill("1").join("") + "0" + Array(binary.length - zeroCount - firstOnes).fill("1").join("")
};
    

