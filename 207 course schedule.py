class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses
        in_nodes = [[] for x in range(numCourses)]
        for pair in prerequisites:
            degrees[pair[0]] += 1 #for each course, how many prerequisites
            in_nodes[pair[1]].append(pair[0]) #for each prerequisite, all the courses dependent on them
        courses = set(range(numCourses)) #course set for remove when done
        
        flag = True
        while flag and len(courses):
            flag = False #flag for having prerequisites
            removeList = []
            for crs in courses:
                if degrees[crs] == 0:
                    for in_node in in_nodes[crs]: degrees[in_node] -= 1
                    removeList.append(crs)
                    flag = True
            for x in removeList: courses.remove(x)
        return len(courses) == 0
                
    # logging version
    #def canFinish(self, numCourses, prerequisites):
    #    degrees = [0] * numCourses
    #    in_nodes = [[] for x in range(numCourses)]
    #    #print "out degrees",degrees
    #    #print "in nodes",in_nodes
    #    
    #    for pair in prerequisites:
    #        degrees[pair[0]] += 1
    #        in_nodes[pair[1]].append(pair[0])
    #    courses = set(range(numCourses))
    #    print "out degrees",degrees
    #    print "in nodes",in_nodes,"\n"
    #    
    #    flag = True
    #    #ans = []
    #    while flag and len(courses):
    #        print "flag",flag,"len(courses)",len(courses)
    #        flag = False
    #        removeList = []
    #        print "removeList",removeList,"\n"
    #        for crs in courses:
    #            if degrees[crs] == 0:
    #                print "course",crs,"out degree is 0"
    #                for in_node in in_nodes[crs]:
    #                    print "in_node",in_node,"degrees[in_node]-1"
    #                    degrees[in_node] -= 1
    #                print "degrees",degrees
    #                print "removeList.append crs",crs
    #                removeList.append(crs)
    #                print "flag=True, could move forward\n"
    #                flag = True
    #            else:
    #                print "course",crs
    #                print "degrees",degrees
    #                print "removeList",removeList
    #                print "flag=False\n"
    #        for x in removeList:
    #            #ans.append(x)
    #            print "removeList member",x,"removed from courses"
    #            courses.remove(x)
    #        print
    #    #return [[], ans][len(courses) == 0]
    #    return len(courses) == 0
        
a=Solution()
#print a.canFinish(4,[[1,0],[2,1],[3,0],[3,1]])
#print a.canFinish(4,[[1,0],[3,0],[3,1],[0,2]])
print a.canFinish(4,[[1,0],[2,1],[3,0],[0,1]])