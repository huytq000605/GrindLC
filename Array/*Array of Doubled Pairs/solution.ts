function canReorderDoubled(arr: number[]): boolean {
    arr.sort((a, b) => {
        if (a < 0 && b < 0) {
            return b - a;
        } else {
            return a - b;
        }
    });
    let freq = new Map();
    for (let i = 0; i < arr.length; i++) {
        if (!freq.has(arr[i])) {
            freq.set(arr[i], []);
        }
        freq.get(arr[i]).push(i);
    }
    let indexUsed = new Set();
    for (let i = 0; i < arr.length; i++) {
        if (indexUsed.has(i)) continue;
        if (arr[i] === 0) {
            if (freq.has(0) && freq.get(0).length % 2 === 0) {
                continue;
            } else {
                return false;
            }
        } else {
            if (freq.has(2 * arr[i]) && freq.get(2 * arr[i]).length > 0) {
                indexUsed.add(freq.get(2 * arr[i]).shift());
            } else {
                return false;
            }
        }
    }
    return true;
}
