function entityParser(text: string): string {
    let dict = new Map()
    dict.set("&quot;", `"`);
    dict.set("&apos;", `'`);
    dict.set("&amp;", `&`);
    dict.set("&gt;", `>`);
    dict.set("&lt;", `<`);
    dict.set("&frasl;", `/`);
    let stack = []
    let result = text
    for(let i = 0; i < result.length; i++) {
        if(result[i] == "&") {
            stack.push(i)
            continue
        }
        if(result[i] == ";") {
            if(stack.length === 0) continue;
            let start = stack.pop()
            let end = i;
            let str = result.slice(start, end + 1)
            if(dict.has(str)) {
                result = result.slice(0, start) + dict.get(str) + result.slice(end+1)
                i -= str.length - 1
            }
        }
        
    }
    return result
};