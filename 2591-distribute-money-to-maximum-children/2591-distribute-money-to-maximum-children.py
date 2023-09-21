class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        
        # give every one 1$        
        money = money - children
        
        # let n children have 8$
        n = money // 7
        
        if n == 0:
            return 0
        
        # remaining after giving 8$
        money -= 7 * n                
        
        if n >= children:
            if n == children and money == 0:
                return children
            return children - 1                
        
        # if we are left with 3 dollars and only one child
        # give the child 2$ and one child will need to have 9$
        if money == 3 and children - n == 1:            
            return n - 1                
                
        # all requirements fullfilled
        return n