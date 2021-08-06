function alertNames(keyName: string[], keyTime: string[]): string[] {
    let key = Array(keyName.length).fill(0).map((_, idx) => [keyName[idx], keyTime[idx]])
    key.sort((a,b) => a[0].localeCompare(b[0]) || a[1].localeCompare(b[1]))
    let result = []
    let alerted = new Set()
    for(let i = 2; i < key.length; i++) {
        if(alerted.has(key[i][0])) continue
        if(convert(key[i][1]) - convert(key[i - 2][1]) <= 60 && key[i][0] === key[i - 2][0] ) {
            result.push(key[i][0])
            alerted.add(key[i][0])
        }
    }
    return result
};
    
function convert(str) {
    let hour = Number(str[0]) * 10 + Number(str[1])
    let minute = Number(str[3]) * 10 + Number(str[4])
    let result = hour*60 + minute
    return result
}