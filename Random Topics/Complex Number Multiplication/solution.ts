function complexNumberMultiply(num1: string, num2: string): string {
    let n1 = num1.split("+")
    let re1 = Number(n1[0])
    let im1 = Number(n1[1].slice(0, n1[1].length - 1))
    
    let n2 = num2.split("+")
    let re2 = Number(n2[0])
    let im2 = Number(n2[1].slice(0, n2[1].length - 1))
    
    let re = re1 * re2 - im1 * im2
    let im = re1*im2 + re2*im1
    return `${re}+${im}i`
};