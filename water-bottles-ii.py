class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        """
        Not possible condition refers to emptyBottles < numOfExchanges
        The algo is -> In turn 1, drink all the bottles, then exchange the bottles till possible.
        Then again drink all the water collected and repeat the process till not possible anymore.
        """
        fullBottles = numBottles
        emptyBottles = 0
        bottlesDrunk = 0
        while fullBottles != 0 or emptyBottles >= numExchange:
            bottlesDrunk += fullBottles
            emptyBottles += fullBottles
            fullBottles = 0
            while emptyBottles >= numExchange:
                emptyBottles -= numExchange
                fullBottles += 1
                numExchange += 1
        return bottlesDrunk

