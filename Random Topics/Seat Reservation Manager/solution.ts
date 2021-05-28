// Just a straight solution with no optimized
// This can be done very fast by using priority queue
class SeatManager {
    seats: Array<number>;
    min: number;
    constructor(n: number) {
        this.seats = Array(n).fill(0)
        this.min = 0
    }

    reserve(): number {
        this.seats[this.min] = 1;
        const seatNumber = this.min + 1
        for(let i = this.min + 1; i < this.seats.length; i++) {
            if(!this.seats[i]) {
                this.min = i;
                break
            }
            if(i == this.seats.length - 1) {
                this.min = this.seats.length - 1
            }
        }

        return seatNumber
    }

    unreserve(seatNumber: number): void {
        let index = seatNumber - 1;
        if(index < this.min) {
            this.min = index
        }
        this.seats[index] = 0
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * var obj = new SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */