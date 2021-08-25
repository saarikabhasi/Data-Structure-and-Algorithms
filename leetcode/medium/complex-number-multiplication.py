class Solution:
    def findvariables(self,num):
        """
        This function seperates given equation into real, imaginary part, the sign between the real and imaginary part and optional argument
        
        example: "1+-1i"
        here the optional argument in + 
        
        The optional argument is added in the sign part of the final result 
        
        
        """
        sign  = ""
        real = ""
        img  = "" 
        op = ""
        for i in range(len(num)):
            if num[i] == "+" or num[i] == "-" and real != "":

                if sign == "":
                    sign = num[i]
                    
                else:
                    if op == "":
                        op = sign
                    if sign == "+" and num[i] == "-":
                        sign = "-"
                    elif sign == "-" and num[i] == "-":
                        sign = "+"
            else:
                if sign == "":
                    real+=num[i]
                else:
                    if num[i]!="i":
                        img += num[i]
        return int(real),int(img),sign,op
            
        
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        sign = {"+":+1,"-":-1}
        
        real1,img1,sign1,op1 = self.findvariables(num1)
        real2,img2,sign2,op2 = self.findvariables(num2)
        

        
       
        img1 = sign[sign1]*img1
        img2 = sign[sign2]*img2
       
        m = str(real1*img2 + real2*img1) + "i"
        
        if (m[0] == "-" or m[0] == "+") and m[0] !=sign1:
            m = sign1 + m    
       
        r = real1*real2
        i = img1 * img2 * -1
        
        if op1 !="" or op2 != "":
            if op1 == op2:
                result = str(r + i) +op1+ m
            else:
                if m[0] == op1 or m[0] == op2:
                    result = str(r + i) + m
                else:
                    result =str(r + i) +op1+op2+ m
        else:
          
            if m[0]!="+":
                result =str(r + i) +"+"+ m
            else:
                result =str(r + i) + m
        return result
        

         
      
        
       
                
                
            
        
        
                

            
        
