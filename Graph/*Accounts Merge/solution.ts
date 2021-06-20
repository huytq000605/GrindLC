function accountsMerge(accounts: string[][]): string[][] {
    let graph = new Map<string, Set<string>>()
    
	// Build a graph 
    for(let account of accounts) {
        for(let i = 1; i < account.length; i++) {
            if(i === 0) continue;
            if(!graph.has(account[i])) graph.set(account[i], new Set())
            if(i === account.length - 1) continue; // For if account only have 1 email
            if(!graph.has(account[i+1])) graph.set(account[i+1], new Set())
            graph.get(account[i]).add(account[i+1])
            graph.get(account[i+1]).add(account[i])
        }
    }
    
	// DFS function
    function dfs(emails: string[], email: string, seen: Map<string, boolean>) {
        if(seen.has(email)) return;
        seen.set(email, true)
        emails.push(email)
        let connectedEmails = graph.get(email)
        for(let connectedEmail of connectedEmails.values()) {
            dfs(emails, connectedEmail, seen)
        }
    }
    
    let result = []
	// Seen map for all emails
    let seen = new Map<string, boolean>()
    
    for(let account of accounts) {
        let userName = account[0]
        let emails = []
        for(let i = 1; i < account.length; i++) {
            dfs(emails, account[i], seen)
        }
        if(emails.length === 0) continue; // All these emails in this original account has been merged
        emails.sort() // Sort the emails
        let pushingAccount = [userName, ...emails]
        result.push(pushingAccount)
    }
    
    return result
};

