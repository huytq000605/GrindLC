class TweetCounts {
    map: Map<string, number[]>
    constructor() {
        this.map = new Map()
    }

    recordTweet(tweetName: string, time: number): void {
        if(!this.map.has(tweetName)) {
            this.map.set(tweetName, [])
        }
        this.map.get(tweetName).push(time)
    }

    getTweetCountsPerFrequency(freq: string, tweetName: string, startTime: number, endTime: number): number[] {
        let delta
        switch(freq) {
            case "minute":
                delta = 60
                break
            case "hour":
                delta = 3600
                break
            case "day":
                delta = 86400
                break
        }
        let result = Array(Math.ceil((endTime - startTime + 1)/(delta))).fill(0)
        for(let num of this.map.get(tweetName)) {
            if(num < startTime || num > endTime) continue
            let index = Math.floor((num - startTime + 1) / delta)
            result[index]++
        }
        return result
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * var obj = new TweetCounts()
 * obj.recordTweet(tweetName,time)
 * var param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
 */