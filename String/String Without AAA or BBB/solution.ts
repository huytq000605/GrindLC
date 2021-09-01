function strWithout3a3b(a: number, b: number): string {
    let result = ""
    while(a > 0 || b > 0) {
        if(a >= b) {
            if(result.length >= 2 && result[result.length - 1] === "a" && result[result.length - 2] === "a") {
                b--
                result += "b"
            } else {
                a--
                result += "a"
            }
        } else {
            if(result.length >= 2 && result[result.length - 1] === "b" && result[result.length - 2] === "b") {
                a--
                result += "a"
            } else {
                b--
                result += "b"
            }
        } 
    }
    return result
};