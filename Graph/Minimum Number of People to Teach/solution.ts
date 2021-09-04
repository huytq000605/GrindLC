function minimumTeachings(n: number, languages: number[][], friendships: number[][]): number {
    let graph = new Map()
    for(let fr of friendships) {
        if(!graph.has(fr[0] - 1)) graph.set(fr[0] - 1, [])
        if(!graph.has(fr[1] - 1)) graph.set(fr[1] - 1, [])
        graph.get(fr[0] - 1).push(fr[1] - 1)
        graph.get(fr[1] - 1).push(fr[0] - 1)
    }
    let teachMap = Array(n + 1).fill(0)
    let seen = new Set() // Number of people that have at least one friend that he/she cannot talk to
    
    for(let person = 0; person < languages.length; person++) {
        if(graph.has(person)) {
            let canSpeak = new Set()
            for(let lang of languages[person]) {
                canSpeak.add(lang)
            }
            for(let friend of graph.get(person)) { // Check if this person can speak to each friend?
                let canSpeakToPerson = false
                for(let lang of languages[friend]) {
                    if(canSpeak.has(lang)) {
                        canSpeakToPerson = true
                        break
                    }
                }
                if(!canSpeakToPerson) { // If this person cant speak to this friend
                    if(!seen.has(friend))
                    for(let lang of languages[friend]) teachMap[lang]++ // Dont need to teach this lang
                    if(!seen.has(person))
                    for(let lang of languages[person]) teachMap[lang]++
                    seen.add(person)
                    seen.add(friend)
                }
            }
        }
    }
    
    let result = seen.size - Math.max(...teachMap) // Since we can only teach 1 language, we need to choose the language that have the greatest people've already know it
    
    return result
};