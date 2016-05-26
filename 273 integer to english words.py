class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0: return "Zero"
        mp={0:"",
            1:"One", 2:"Two",  3:"Three",4:"Four",5:"Five",
            6:"Six", 7:"Seven",8:"Eight",9:"Nine",10:"Ten",
            11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",
            16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",
            30:"Thirty",40:"Forty",50:"Fifty",
            60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",100: "Hundred",
            1000: "Thousand",1000000: "Million",1000000000: "Billion"}
        for i in range(21,100):
            if i%10==0: continue
            mp[i]=mp[i/10*10]+' '+mp[i%10]
        for i in range(100,1000):
            mp[i]=(mp[i/100]+' Hundred '+mp[i%100]).strip()
        if num<1000: return mp[num]
        
        res=[]
        for k in [1000000000,1000000,1000]:
            cnt=num/k
            if cnt>0:
                res.append(mp[cnt])
                res.append(mp[k])
                num=num%k
        res.append(mp[num])
        return ' '.join(res).strip()

    def numberToWords2(self, num):
        lv1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten \
               Eleven Twelve Thirteen Fourteen Fifteen \
               Sixteen Seventeen Eighteen Nineteen".split()
        lv2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        lv3 = "Hundred"
        lv4 = "Thousand Million Billion".split()
        words, digits = [], 0
        while num:
            token, num = num % 1000, num / 1000
            word = ''
            if token > 99:
                word += lv1[token / 100] + ' ' + lv3 + ' '
                token %= 100
            if token > 19:
                word += lv2[token / 10 - 2] + ' '
                token %= 10
            if token > 0:
                word += lv1[token] + ' '
            word = word.strip()
            if word:
                word += ' ' + lv4[digits - 1] if digits else ''
                words += word,
            digits += 1
        return ' '.join(words[::-1]) or 'Zero'
        
a=Solution()
print a.numberToWords2(123)
print a.numberToWords2(12345)
print a.numberToWords2(1234567)
print a.numberToWords2(1000)