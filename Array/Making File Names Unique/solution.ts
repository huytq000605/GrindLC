function getFolderNames(names: string[]): string[] {
    let nameMap = new Map()
    let result = []
    for(let name of names) {
        if(!nameMap.has(name)) {
            nameMap.set(name, 1)
            result.push(name)
        } else {
            let k = nameMap.get(name)
            while(true) {
                let suffix = `(${k})`
                let append = name + suffix
                if(nameMap.has(append)) {
                    k++
                    continue
                } else {
                    nameMap.set(name, k + 1)
                    result.push(append)
                    nameMap.set(append, 1)
                    break
                }
            }
        }
    }
    return result
};