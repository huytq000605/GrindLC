function numRescueBoats(people: number[], limit: number): number {
    people.sort((a,b) => a-b)
    let rightPointer = people.length -1
    let leftPointer = 0
    let boats = 0
    while(leftPointer <= rightPointer) {
        boats++
        if(leftPointer === rightPointer) {
            return boats
        }
        if(people[rightPointer] + people[leftPointer] <= limit) {
            rightPointer--
            leftPointer++
        } else {
            rightPointer--
        }
    }
    return boats
};