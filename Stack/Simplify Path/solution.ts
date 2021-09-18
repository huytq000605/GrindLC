function simplifyPath(path: string): string {
    let newPath = ""
    for(let i = 0; i < path.length; i++) {
        if(newPath.length && newPath[newPath.length - 1] === "/" && path[i] === "/") continue
        newPath += path[i]
    }
    if(newPath[newPath.length - 1] === "/") newPath = newPath.slice(1, newPath.length - 1)
    else newPath = newPath.slice(1)
    let dirs = newPath.split("/")
    let stack = []
    for(let dir of dirs) {
        if(dir === "..") {
            if(stack.length) stack.pop()
        } else if(dir === ".") {
            
        } else {
            stack.push(dir)
        }
    }
    return "/" + stack.join("/")
};