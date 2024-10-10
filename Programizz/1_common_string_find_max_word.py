#find the length og the  longest common prerfix
class LongestCommonPrefix:
    def find_length(self,str1,str2):
        min_length =min(len(str1),len(str2))
        length=0
        
        for i in range(min_length):
            if str1[i] == str2[i]:
                length +=1
            
            else:
                break
            
        
        return length
        

lcp =LongestCommonPrefix()
arg1="Fiboonak"
arg2="Fiboonoookiii"

print(lcp.find_length(arg1,arg2))
            
    
    