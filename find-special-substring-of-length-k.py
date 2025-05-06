class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        tempk = 0
        oldChar = ""
        for letter in s:
            if oldChar!=letter:
                # New letter found
                if tempk==k:
                    return True
                tempk=1
                oldChar = letter
            else:
                tempk+=1
        if tempk==k:
            return True
        return False
            