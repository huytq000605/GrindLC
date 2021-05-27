function kthSmallest(matrix: number[][], k: number): number {
    let result = []
    let idxArr = Array(matrix.length).fill(0)
    let row = 0;
    for(let i = 0; i < k; i++) {
        let min = Number.MAX_SAFE_INTEGER
        for(let j = 0; j < matrix.length; j++) {
            // Can remove because of javascript hah xD
            // if(idxArr[j] == matrix.length) { 
            //     continue
            // }
            if(matrix[j][idxArr[j]] < min) {
                min = matrix[j][idxArr[j]]
                row = j
            }
            
        }
        result.push(min)
        idxArr[row]++
    }
    return result[k-1]
};