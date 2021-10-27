function subdomainVisits(cpdomains: string[]): string[] {
    let freqMap = new Map()
    for(let cpdomain of cpdomains) {
        let [timeString, domain] = cpdomain.split(" ")
        
        let times = Number(timeString)
        outer:
        while(domain.length) {
            freqMap.set(domain, (freqMap.get(domain) || 0) + times)
            for(let i = 0; i < domain.length; i++) {
                if(domain[i] === ".") {
                    domain = domain.slice(i + 1)
                    continue outer
                }
            }
            break
        }
    }
    
    let result = []
    for(let [domain, freq] of freqMap.entries()) {
        result.push(`${freq} ${domain}`)
    }
    return result
};