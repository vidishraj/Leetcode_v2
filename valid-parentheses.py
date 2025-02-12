class Solution(object):
    def isValid(self, s):
        stack=list()
        for bracket in s:
            if(bracket in ['(', '[','{']):
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if bracket == ')':
                    if stack.pop(-1) != '(' :
                        return False
                elif bracket == ']':
                    if stack.pop(-1) != '[' :
                        return False
                elif bracket == '}':
                    if stack.pop(-1) != '{' :
                        return False
        if len(stack) != 0:
            return False
        return True
                
        """
        :type s: str
        :rtype: bool
        """
        