function maxLength(arr: string[]): number {
    return buildString(arr, 0, "", new Set())
};

function buildString(arr: string[], index: number, current: string, currentMap: Set<string>) {
    if(index === arr.length) {
        return current.length
    }
    let result = current.length
    for(let i = index; i < arr.length; i++) {
        try {
            addToSet(currentMap, arr[i])
        } catch {
            continue
        }
        result = Math.max(result, buildString(arr, i + 1, current + arr[i], currentMap))
        removeFromSet(currentMap, arr[i])
    }
    return result
}

function addToSet(set: Set<string>, str: string) {
    for(let i = 0; i < str.length; i++) {
        if(set.has(str[i])) {
            for(let j = 0; j < i; j++) {
                set.delete(str[j])
            }
            throw new Error("Had this letter")
        }
        set.add(str[i])
    }
}

function removeFromSet(set: Set<string>, str: string) {
    for(let i = 0; i < str.length; i++) {
        set.delete(str[i])
    }
}