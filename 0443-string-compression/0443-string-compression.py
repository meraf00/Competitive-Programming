class Solution:
    def compress(self, chars: List[str]) -> int:        
        write_index = 0
        read_index = 1
        curr = chars[0]
        last_index = 0        
        while read_index < len(chars):
            char = chars[read_index]
            
            if char != curr:
                count = read_index - last_index 
                if count != 1:
                    chars[write_index] = curr
                    write_index += 1
                    for digit in str(count):
                        chars[write_index] = digit 
                        write_index += 1
                else:
                    chars[write_index] = curr                    
                    write_index += 1
                
                curr = char
                last_index = read_index
            
            read_index += 1
        
        count = read_index - last_index 
        if count != 1:
            chars[write_index] = curr
            write_index += 1
            for digit in str(count):
                chars[write_index] = digit 
                write_index += 1
        else:
            chars[write_index] = curr                    
            write_index += 1
            
        return write_index
        