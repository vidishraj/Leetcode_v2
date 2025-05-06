class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        visited = [False for i in range(len(values))]
        totalScore = 0
        def visit(index):
            nonlocal totalScore
            if index<0 or index>=len(values):
                return 
            if visited[index]:
                return
            visited[index] = True
            if instructions[index]=="add":
                totalScore+=values[index]
                visit(index+1)
            else:
                visit(index+values[index])
            
        visit(0)
        return totalScore