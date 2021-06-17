function minFlipsMonoIncr(s: string): number {
    let result = 0
    let numOfOnes = Array(s.length).fill(0) // number of "1" on the left and i position at the index i
    let numOfZeros = Array(s.length).fill(0) // number of "0" on the left and i position at the index i
    let totalOnes = 0 // total "0" in string
    let totalZeros = 0 // total "1" in string
    
    for(let i = 0; i < s.length; i++) {
        if(s[i] == '1') {
            numOfOnes[i] = (numOfOnes[i-1] || 0 )+ 1
            numOfZeros[i] = numOfZeros[i-1] || 0
            totalOnes++
        } else {
            numOfZeros[i] = ( numOfZeros[i-1] || 0 ) + 1
            numOfOnes[i] = (numOfOnes[i-1] || 0 )
            totalZeros++
        }
    }
    
    result = Math.min(totalOnes, s.length - totalOnes) // If we swap all the 0 to 1 or 1 to 0
    
    for(let firstOnePos = 0; firstOnePos < s.length; firstOnePos ++) { // We are choosing the boundary of the string by the first one appear
        let leftFlip = numOfOnes[firstOnePos-1] || 0 // Left flip = total "1" on the left of firstOnePos
        let rightFlip = totalZeros - ( numOfZeros[firstOnePos - 1]  || 0 ) // Right flip = total "0" on the right of firstOnePos
        result = Math.min(result, leftFlip + rightFlip)
    }
    return result
};