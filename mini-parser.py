class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":  
            # Single integer case
            return NestedInteger(int(s))

        stack = []
        runningNum = ""
        current = None  # This will be used to track the current NestedInteger

        for letter in s:
            if letter == "[":
                # Create a new NestedInteger list
                newList = NestedInteger()
                if stack:
                    # Append to the previous NestedInteger
                    stack[-1].add(newList)
                stack.append(newList)
            elif letter.isdigit() or letter == "-":  
                runningNum += letter
            elif letter == "," or letter == "]":
                if runningNum:
                    # Convert runningNum to integer and add to the last NestedInteger
                    stack[-1].add(NestedInteger(int(runningNum)))
                    runningNum = ""
                if letter == "]":  
                    current = stack.pop()  # Finish the nested list
            else:
                continue  # Ignore spaces (though there shouldn't be any)

        return current
