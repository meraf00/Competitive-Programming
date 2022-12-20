"""https://leetcode.com/problems/goal-parser-interpretation/"""

class Solution:
    def interpret(self, command: str) -> str:
        bracket_opened = False
        output = ""
        token = ""
        for char in command:            
            if char == "(":
                bracket_opened = True
                output += token
                token = ""
            elif char == ")":
                bracket_opened = False  
                if token:
                    output += token
                else:
                    output += "o"
                token = ""
            else:
                if bracket_opened:
                    token += char
                else:
                    output += char
        
        return output
            