/*
By observe, we can know no matters where the "0" are, we can push all of it to the left but dont touch the leading "1", the rest will all be 1,
all 0 can transform to 1 except the last one => result
*/

function maximumBinaryString(binary: string): string {
    let leadingOnes;
    let zeros = 0;
    let result = ""
    for(let i = 0; i < binary.length; i++) {
        if(binary[i] === "0") {
            leadingOnes = i
            break;
        }
    }
    if(leadingOnes === undefined) return binary;
    for(let i = leadingOnes; i < binary.length; i++) {
        if(binary[i] == "0") {
            zeros++;
        }
    }
    for(let i = 0; i < leadingOnes + zeros - 1; i++) {
        result += "1";
    }
    result += "0"
    while(result.length < binary.length) {
        result += "1"
    }
    return result
};
    

