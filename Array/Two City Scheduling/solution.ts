function twoCitySchedCost(costs: number[][]): number {
	const pay = [];
	let currentPay = 0;
	for(let i = 0; i < costs.length; i++) {
			currentPay += costs[i][0];
			pay.push(costs[i][1] - costs[i][0]);
	}
	pay.sort((a,b) => a-b);
	for(let i = 0; i < pay.length / 2; i++) {
			currentPay += pay[i]
	}
	return currentPay;
};