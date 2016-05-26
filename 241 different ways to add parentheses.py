class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def dfs(nums, ops):
            #print nums,ops
            if ops:
                for x in range(len(ops)):
                    dfs(nums[:x]+['('+nums[x]+ops[x]+nums[x+1]+')']+nums[x+2:],
                        ops[:x]+ops[x+1:])
            elif nums[0] not in res: res[nums[0]] = eval(nums[0])
                
        import re
        input = re.split(r'(\D)', input)
        nums,ops = [],[]
        for x in input:
            if x.isdigit(): nums.append(x)
            else: ops.append(x)
        res = dict()
        dfs(nums, ops)
        return res.values()
        
    def diffWaysToCompute1(self, input):
        def calc(a, b, o):
            return {'+':lambda x,y:x+y, 
                    '-':lambda x,y:x-y, 
                    '*':lambda x,y:x*y}[o](a, b)
        def dfs(nums, ops):
            if not ops: return [nums[0]]
            ans = []
            for x in range(len(ops)):
                left = dfs(nums[:x+1], ops[:x])
                right= dfs(nums[x+1:], ops[x+1:])
                for l in left:
                    for r in right:
                        ans.append(calc(l, r, ops[x]))
            return ans
        import re
        input = re.split(r'(\D)', input)
        nums, ops = [], []
        for x in input:
            if x.isdigit(): nums.append(int(x))
            else: ops.append(x)
        return dfs(nums, ops)
        
    def diffWaysToCompute2(self,input):
        return [a+b if c == '+' else a-b if c == '-' else a*b
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] \
            or [int(input)]
            
a=Solution()
print a.diffWaysToCompute("2*3-4*5")