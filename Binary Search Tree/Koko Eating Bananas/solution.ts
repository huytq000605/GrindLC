function minEatingSpeed(piles: number[], h: number): number {
    let min = 1;
    let max = 0;
    for(let i = 0; i < piles.length; i++) {
        max = Math.max(max, piles[i]);
    }
    while(min < max) {
        let speed = Math.floor((max+min)/2);
        let time = timeKokoNeed(piles, speed);
        if(time > h) {
            min = speed + 1;
        }
        else {
            max = speed;
        }
    }
    return min
};

function timeKokoNeed(piles: number[], speed: number): number {
    let result = 0;
    for(let i = 0; i < piles.length; i++) {
        result += Math.ceil(piles[i]/speed)
    }
    return result;
}