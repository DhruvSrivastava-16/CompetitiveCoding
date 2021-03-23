
class Solution(object):
    
    def sm(self,A,B):
        c = [k+j for k in A for j in B]
        return c;
        
    def letterCombinations(self, digits):
        phone = { 
              '2' : ['a','b','c'],
              '3' : ['d','e','f'],
              '4' : ['g','h','i'],
              '5' : ['j','k','l'],
              '6' : ['m','n','o'],
              '7' : ['p','q','r','s'],
              '8' : ['t','u','v'],
              '9' : ['w','x','y','z']
            }
    
        
        l = len(digits)
        ans = []
    
        if l == 0:
            return (ans);
                
        if l == 1:
            ans = phone[digits[0]]
            return (ans); 
        
        count = 0;
        ans = phone[digits[count]]
        count += 1;
        
        
        while(count<l):
            ans = self.sm(ans,phone[digits[count]]);
            count+=1;
            
        return ans;
        

if __name__ == '__main__':
        
   
    digits = input("Digits: ")
    
    S = Solution();
    answer = S.letterCombinations(digits)
    print(answer);
    
        
        