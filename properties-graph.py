class Solution:
    @staticmethod
    def intersect(lista, listb):
        return list(set(lista) & set(listb))
        
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        # First make the graph (adj matrix-> undirected)
        n = len(properties)
        m = len(properties[0])
        graph = [[None for i in range(n)] for i in range(n)]
        edges=0
        for i in range(n):
            for j in range(i+1, n):
                if graph[i][j] is None and graph[j][i] is None and  len(self.intersect(properties[i], properties[j]))>=k:
                    edges += 1
                    graph[i][j] = True
                    graph[j][i] = True
        res = 0
        
        unconnected = 0 
        for i in range(n):
            ne = False
            for j in range(n):
                if graph[i][j]:
                    ne = True
            if not ne:
                unconnected+=1
        # Now we run bfs till we have all visited all components
        visited = 0 
        q = collections.deque()
        while visited<edges:
            res+=1
            edgeFound = False
            for i in range(n):
                for j in range(i+1, n):
                    if graph[i][j]:
                        edgeFound = True
                        q.append(i)
                        break
                if edgeFound:
                    break
            while len(q)>0:
                curr = q.popleft()
                for i in range(n):
                    if graph[curr][i]:
                        visited+=1
                        graph[curr][i] = None
                        graph[i][curr] = None
                        q.append(i)

        res += unconnected 
        return res