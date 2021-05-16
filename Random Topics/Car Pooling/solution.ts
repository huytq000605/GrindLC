function carPooling(trips: number[][], capacity: number): boolean {
    let currentPeople = [];
    for(let trip of trips) {
        for(let i = trip[1]; i < trip[2]; i++) {
            currentPeople[i] = (currentPeople[i] || 0) + trip[0];
        }
    }
    for(let ele of currentPeople) {
        if(ele > capacity) return false
    }
    
    return true;
};