from collections import defaultdict


def accountsMerge(accounts):
    """
    {
    "john@gmail.com" : [0,1,2,3]

    }
    
    
    
    """
    email_to_accounts = defaultdict(list)
    
    for num, account in enumerate(accounts):
        for i in range(1, len(account)):
            email = account[i]
            email_to_accounts[email].append(num)
        

    visited_accounts = [False] * len(accounts)
    res = []
    
    def dfs(i, emails):
        if visited_accounts[i]:
            return
        
        visited_accounts[i] = True

        for email_index in range(1, len(accounts[i])):
            email = accounts[i][email_index]
            emails.add(email)
            for neighbour in email_to_accounts[email]:
                dfs(neighbour, emails)
    
    for num, account in enumerate(accounts):
        if visited_accounts[num]:
            continue
        emails = set()
        name = account[0]
        dfs(num, emails)
        res.append([name] + sorted(emails))
    
    return res

    
    