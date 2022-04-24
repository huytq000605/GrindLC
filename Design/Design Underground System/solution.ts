class UndergroundSystem {
	mapCount;
	mapTime;
	constructor() {
			this.mapCount = new Map()
			this.mapTime = new Map()
	}

	checkIn(id: number, stationName: string, t: number): void {
			this.mapTime.set(id, {stationName, start: t});
	}

	checkOut(id: number, stationName: string, t: number): void {
			const info = this.mapTime.get(id);
			this.mapTime.delete(id);
			this.mapTime.set(`${info.stationName}-${stationName}`, ( this.mapTime.get(`${info.stationName}-${stationName}`) || 0 )+ t - info.start );
			this.mapCount.set(`${info.stationName}-${stationName}`, (this.mapCount.get(`${info.stationName}-${stationName}`) || 0 )+ 1)
	}

	getAverageTime(startStation: string, endStation: string): number {
		return  this.mapTime.get(`${startStation}-${endStation}`) / this.mapCount.get(`${startStation}-${endStation}`)
	}
}

/**
* Your UndergroundSystem object will be instantiated and called as such:
* var obj = new UndergroundSystem()
* obj.checkIn(id,stationName,t)
* obj.checkOut(id,stationName,t)
* var param_3 = obj.getAverageTime(startStation,endStation)
*/