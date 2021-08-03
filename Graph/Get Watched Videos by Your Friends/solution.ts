function watchedVideosByFriends(watchedVideos: string[][], friends: number[][], id: number, level: number): string[] {
    let map = new Map()
    let queue = [[0, id]]
    let seen = new Set()
    seen.add(id)
    while(queue.length) {
        let [depth, current] = queue.shift()
        if(depth === level) {
            for(let video of watchedVideos[current]) {
                map.set(video, (map.get(video) || 0) + 1)
            }
        }
        
        if(depth < level) {
            for(let friend of friends[current]) {
                if(!seen.has(friend)) {
                    queue.push([depth + 1, friend])
                    seen.add(friend)
                }
                    
            } 
        }
        
    }
    let result = []
    
    for(let [key, value] of map.entries()) {
        result.push([key, value])
    }
    
    result.sort((a,b) => {
        if(a[1] > b[1]) return 1
        if(a[1] === b[1]) {
            return a[0].localeCompare(b[0])
        }
        return -1
    })
    
    result = result.map((res) => res[0])
    return result
    
};
