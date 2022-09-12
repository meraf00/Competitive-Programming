"""
https://leetcode.com/problems/integer-to-english-words/
"""

class Solution:
    def get_digits(self, num: int) -> int:
        return len(str(num))        
    
    def name3dig(self, num: int, offset: int = 0) -> str:
        digX = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        dig1X = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        digXX = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        postfixes = ["", "Thousand", "Million", "Billion"]
        
        postfix = postfixes[offset]
        
        digits = self.get_digits(num)
        
        output = ""
        if digits == 1:            
            output = digX[num]
            if offset != 0 and num == 0:
                output = ""
        
        elif digits == 2:                        
            if str(num)[0] == "1":
                output = "%s" % dig1X[num % 10]
            
            elif str(num)[1] == "0":                
                output = "%s" % digXX[int(str(num)[0]) - 2]
            else:
                output = "%s %s" % (digXX[int(str(num)[0]) - 2], digX[num % 10])
        
        elif digits == 3:            
            output = "%s Hundred" % digX[int(str(num)[0])]
             
            if str(num)[1:] == "00":
                pass
            
            elif str(num)[1] == "0":
                output += " %s" % digX[num % 10]
                
            elif str(num)[1] == "1":
                output += " %s" % dig1X[num % 10]
            
            elif str(num)[2] == "0":                
                output += " %s" % digXX[int(str(num)[1]) - 2]
            else:
                output += " %s %s" % (digXX[int(str(num)[1]) - 2], digX[num % 10])
            
        if postfix and output:
            return output + " " + postfix
        else:
            return output
        

    def numberToWords(self, num: int) -> str:
        grouped = []
        
        num = str(num)
                
        i = len(num) - 1
        
        current = ""
        while i > -1:            
            while i > -1 and len(current) < 3:
                current += num[i]
                i -= 1
            grouped.append("".join(list(reversed(current))))
            current = ""
        grouped.reverse()                                        
        
        grouped = list(map(int, grouped))
        
        output = ""
        for i, g in enumerate(reversed(grouped)):
            group_name = self.name3dig(g, i)
            if group_name == "Zero" and i < len(grouped) - 1:
                continue
            if group_name:
                output = group_name + " " + output            
            
        return output.strip()