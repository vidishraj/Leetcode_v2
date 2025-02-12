class Solution(object):
    valueList = []
    solution = 0
    kValue = 0

    def recHelper(self, adjacencyMat, index, visited):
        #print(index, visited)
        if len(adjacencyMat[index]) == 1 and visited[adjacencyMat[index][0]] == 1:
            return self.valueList[index]
        totalSum = self.valueList[index]
        visited[index]=1
        for sibling in adjacencyMat[index]:
            if sibling != 0 and visited[sibling]!=1:
                visited[sibling] = 1
                sumValue = self.recHelper(adjacencyMat, sibling, visited)
                #print("sumValue",sumValue, sibling)
                totalSum += sumValue
                if (sumValue % self.kValue == 0):
                    self.solution += 1
        #print("TotalSum", totalSum)
        # #print("totalSum", totalSum)
        # if totalSum%self.kValue==0:
        #     self.solution+=1
        return totalSum

    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        # Convert it to a adjacency matrix and then traverse it backwards
        adjacencyMat = []
        visited = []
        self.kValue = k
        self.valueList = values
        for i in range(0, n):
            visited.append(0)
            adjacencyMat.append([])
        for edge in edges:
            adjacencyMat[edge[0]].append(edge[1])
            adjacencyMat[edge[1]].append(edge[0])
        for num in adjacencyMat[0]:
            visited[0]=1
            sumValue = self.recHelper(adjacencyMat, num, visited)
            #print("finalSums",sumValue)
            if sumValue%k==0:
                self.solution+=1
        #print(adjacencyMat)
        return self.solution+1