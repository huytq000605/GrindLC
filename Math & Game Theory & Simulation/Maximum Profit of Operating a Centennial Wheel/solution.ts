function minOperationsMaxProfit(customers: number[], boardingCost: number, runningCost: number): number {
    let currentWaiting = 0
    let currentPeople = 0
    let profit = 0
    let rotate = 0
    let result = [0, -1]
    while(rotate < customers.length || currentWaiting > 0) {
        if(rotate < customers.length) currentWaiting += customers[rotate]
        rotate++
        profit += Math.min(currentWaiting, 4) * boardingCost - runningCost
        currentWaiting -= Math.min(currentWaiting, 4)
        if(profit > result[0]) {
            result = [profit, rotate]
        }
    }
    return result[1]
};