/*
Binary Search Tree
*/

function minDays(bloomDay: number[], m: number, k: number): number {
    if(k*m > bloomDay.length) return -1
    let min = 1;
    let max = 1000000000
    while(min < max) {
        let days = Math.floor((max+min)/2);
        let flower = 0;
        let bouquet = 0;
        for(let i = 0; i < bloomDay.length; i++) {
            if(days >= bloomDay[i]) {
                flower++
                if(flower === k) {
                    bouquet++
                    flower = 0
                }
            }
            else {
                flower = 0
            }
        }
        if(bouquet >= m) {
            max = days;
        }
        else {
            min = days + 1;
        }
    }
    return min
    
    
};