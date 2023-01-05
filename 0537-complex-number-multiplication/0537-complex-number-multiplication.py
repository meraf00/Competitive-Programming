class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        
        num1_real = int(num1[0])
        num1_imaginary = num1[1]
        
        # remove the character i         
        num1_imaginary = int(num1_imaginary[:-1])
        
        num2_real = int(num2[0])
        num2_imaginary = num2[1]
        
        # remove the character i         
        num2_imaginary = int(num2_imaginary[:-1])
        
        
        product_real = num1_real * num2_real - num1_imaginary * num2_imaginary
        product_imaginary = num1_real * num2_imaginary + num2_real * num1_imaginary
        
        product = f"{product_real}+{product_imaginary}i"
        
        return product
        
        