function computeArea(ax1: number, ay1: number, ax2: number, ay2: number, bx1: number, by1: number, bx2: number, by2: number): number {
    let left = Math.max(ax1, bx1)
    let top = Math.min(ay2, by2)
    let right = Math.min(ax2, bx2)
    let bottom = Math.max(ay1, by1)
    let overlap = 0
    if(left < right && bottom < top) {
        overlap = (right - left) * (top - bottom)
    }
    return (ax2 - ax1) * (ay2 - ay1) + (by2 - by1) * (bx2 - bx1) - overlap
};