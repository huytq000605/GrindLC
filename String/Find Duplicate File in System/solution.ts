function findDuplicate(paths: string[]): string[][] {
    let map = new Map();
    let result = []
    for(let path of paths) {
        const longString = path.split(' ')
        const directory = longString[0] + '/';
        for(let [index, value] of longString.entries()) {
            if(index === 0) continue;
            const temp = value.split('(');
            const content = temp[1];
            const fileName = temp[0];
            const location = directory + fileName;
            if(!map.get(content)) map.set(content, []);
            map.get(content).push(location);
        }
    }
    for(let value of map.values()) {
        if(value.length >= 2)
        result.push(value);
    }
    return result;
};
