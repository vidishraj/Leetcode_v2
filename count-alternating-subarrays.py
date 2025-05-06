class Solution:

    def runFormula(self, num):
        return num*num-((num*(num+1))/2)

    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        """
        for [1,0] -> 2
        for [0,1,0]->[0,1] and [1,0] are two other ones (3 individual)-> 6 total
        for [0,1,0,1]-> [0,1],[1,0],[0,1],[0,1,0],[1,0,1] -> 10
        for [0,1,0,1,0]-> [0,1],[1,0],[0,1],[1,0],[0,1,0],[1,0,1],[0,1,0],

        use formula-> \U0001d45b\U0001d458−\U0001d458(\U0001d458+1)/2:
         for 2->4-3->1
         for 3-> 3(3) -(3)(4)/2= 3
         for 4-> 16-10->6
         for 5->25-15->10

        :param nums:
        :return:
        """

        currentLen=1
        total=0
        for index in range(len(nums)-1):
            if nums[index]!=nums[index+1]:
                currentLen+=1
            else:
                total += self.runFormula(currentLen+1)
                # print(total)
                currentLen=1
        total += self.runFormula(currentLen + 1)
        return int(total)