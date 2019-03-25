from collections import defaultdict 
  
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
  
        # default dictionary to store graph 
        self.graph= defaultdict(list) 
  
    # function to add an edge to undirected graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 
  
    # A recursive function to call DFS starting from v. 
    # It returns true if vDegree of v after processing is less 
    # than k else false 
    def DFSUtil(self,v,visited,vDegree,k): 
  
        # Mark the current node as visited 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
  
            # vDegree of v is less than k, then vDegree of 
            if vDegree[v] < k: 
                vDegree[i] = vDegree[i] - 1
  
            # If adjacent is not processed, process it 
            if visited[i]==False: 
                if (self.DFSUtil(i,visited,vDegree,k)): 
                    vDegree[v]-=1
  
        # Return true if vDegree of v is less than k 
        return vDegree[v] < k 
  
  
    # Prints k cores of an undirected graph 
    def printKCores(self,k): 
  
        # INITIALIZATION 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
  
        # Store vDegrees of all vertices 
        vDegree = [0]*self.V 
        for i in self.graph: 
                vDegree[i]=len(self.graph[i]) 
  
        # choose any vertex as starting vertex 
        self.DFSUtil(0,visited,vDegree,k) 
  
        for i in range(self.V): 
            if visited[i] ==False: 
                self.DFSUtil(i,k,vDegree,visited) 
  
        # PRINTING K CORES 
        print("\n K-cores: ")
        for v in range(self.V): 
  
            # Only considering those vertices which have 
            # vDegree >= K after DFS 
            if vDegree[v] >= k: 
                print(str("\n [ ") + str(v) + str(" ]")) 
  
                # Traverse adjacency list of v and print only 
                # those adjacent which have vvDegree >= k 
                # after DFS 
                for i in self.graph[v]: 
                    if vDegree[i] >= k: 
                        print("-> " + str(i))
        
    def writeKCores(self,outputfile, k): 
        file = open(outputfile, "w+")
        
        visited = [False]*self.V 
  
        # Store vDegrees of all vertices 
        vDegree = [0]*self.V 
        for i in self.graph: 
                vDegree[i]=len(self.graph[i]) 
  
        # choose any vertex as starting vertex 
        self.DFSUtil(0,visited,vDegree,k) 
  
        # DFS traversal to update vDegrees of all 
        # vertices,in case they are unconnected 
        for i in range(self.V): 
            if visited[i] ==False: 
                self.DFSUtil(i,k,vDegree,visited) 
  
        # PRINTING K CORES 
        print("\n K-cores: ")
        for v in range(self.V): 
  
            # Only considering those vertices which have 
            # vDegree >= K after DFS 
            if vDegree[v] >= k: 
                file.write(str("\n [ ") + str(v) + str(" ]")) 
  
                # Traverse adjacency list of v and print only 
                # those adjacent which have vvDegree >= k 
                # after DFS 
                for i in self.graph[v]: 
                    if vDegree[i] >= k: 
                        file.write("-> " + str(i)) 
        