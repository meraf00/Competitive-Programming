class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n_accounts = len(accounts)
        
        email_to_idx = defaultdict(lambda : -1)
        
        rep = {i : i for i in range(n_accounts)}
        
        rank = [1] * n_accounts
        
        def find(node):
            parent = node
            while parent != rep[parent]:
                parent = rep[parent]
            
            while node != rep[node]:
                temp = rep[node]
                rep[node] = parent
                node = temp
            
            return parent
                
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            
            
            if rank[xRep] >= rank[yRep]:
                rep[yRep] = xRep
                rank[xRep] += rank[yRep]
            
            else:
                rep[xRep] = yRep
                rank[yRep] += rank[xRep]
            
        
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_idx:                    
                    union(email_to_idx[email], idx)
                
                else:
                    email_to_idx[email] = idx
        
        
        user_accounts = defaultdict(set)
        
        for idx, account in enumerate(accounts):
            user_id = find(idx)            
                                    
            user_accounts[user_id].update(account[1:])
        
        
        answer = []
        
        for user_id, emails in user_accounts.items():
            name = accounts[user_id][0]
            answer.append([name, *sorted(emails)])
        
        return answer
            
            