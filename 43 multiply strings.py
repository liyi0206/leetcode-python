class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)*int(num2))
        
    def multiply2(self,num1,num2):
        num1, num2 = num1[::-1], num2[::-1]
        tmp = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp[i+j] += int(num1[i]) * int(num2[j])
        carry, res = 0, []
        for digit in tmp:
            sum = carry+digit
            carry = sum/10
            res.insert(0, str(sum%10))
        while len(res)>1 and res[0]=="0": del res[0]
        return ''.join(res)
            
        
a=Solution()
print a.multiply("36","16") #"576"