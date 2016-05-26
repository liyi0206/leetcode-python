class Solution(object):
    def findItinerary(self, tickets): #best efficiency
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # need to use up all tickets - must use DFS
        # need to return an itinerary with top lexical order
        
        self.mp={}
        for c1,c2 in reversed(sorted(tickets)):
            if c1 not in self.mp: self.mp[c1]=[c2]
            else: self.mp[c1].append(c2)

        self.res=[]
        self.bt("JFK")
        return self.res[::-1] #reverse res
        # as the last city is the first to append, need to reverse res at last
            
    def bt(self,c):
        while c in self.mp and self.mp[c]: 
            self.bt(self.mp[c].pop())
        self.res.append(c)
        # we could sort city names, and pop from queue head each time;
        # or sort city names descendingly, and pop from end, with o(1) time. 

class Solution1(object): #most intuitive
    def findItinerary(self, tickets):
        self.mp={}
        for c1,c2 in sorted(tickets):
            if c1 not in self.mp: self.mp[c1]=[c2]
            else: self.mp[c1].append(c2)
        self.res=[]
        self.bt("JFK")
        return self.res
             
    def bt(self,c):
        while c in self.mp and self.mp[c]: 
            self.bt(self.mp[c].pop(0)) #pop out the lexically smallest
        self.res.insert(0,c) #at last elem (when no more in its mp), add to res front

a=Solution()
print a.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
#["JFK", "MUC", "LHR", "SFO", "SJC"]
print a.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
#["JFK","ATL","JFK","SFO","ATL","SFO"]

class Solution2(object): #get all valid itineraries - TLE for get lexical one
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.mp={}
        for c1,c2 in tickets:
            if c1 not in self.mp: self.mp[c1]=[c2]
            else: self.mp[c1].append(c2)
            
        self.n=len(tickets)+1
        self.res=[]
        self.bt(["JFK"])
        return self.res #return sorted(self.res)[0]
        
    def bt(self,tmp):
        if len(tmp)==self.n: 
            self.res.append(tmp)
            return
        c=tmp[-1]
        if c not in self.mp or not self.mp[c]: return
        
        st=self.mp[c][:]
        for y in st:
            self.mp[c].remove(y)
            self.bt(tmp+[y])
            self.mp[c].append(y)


a=Solution2()               
print a.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
#[["JFK","ATL","JFK","SFO","ATL","SFO"],["JFK","SFO","ATL","JFK","ATL","SFO"]]
#print a.findItinerary([["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],
#["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],
#["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],
#["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],
#["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],
#["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],
#["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],
#["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],
#["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],
#["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],
#["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],
#["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],
#["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],
#["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],
#["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],
#["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],
#["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],
#["AUA","EZE"]])