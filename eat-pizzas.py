class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        eaten = 0
        day = 1
        totalWeight = 0
        # totalWeightOd
        totalDays = int(len(pizzas)/4)
        totalOddDays = math.floor(totalDays/2)
        totalEvenDays= math.floor(totalDays/2)
        if totalDays %2!=0:
            totalOddDays+=1
        eatingIdx = len(pizzas)-1
        # print(totalOddDays, totalEvenDays)
        while totalOddDays!=0:
            totalWeight+=pizzas[eatingIdx]
            totalOddDays-=1
            eatingIdx-=1
        eatingIdx-=1
        while totalEvenDays!=0:
            totalWeight+=pizzas[eatingIdx]
            totalEvenDays-=1
            eatingIdx-=2
            
        return totalWeight
        