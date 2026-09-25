class Solution:
    def isValid(self, s: str) -> bool:


        if len(s) <= 1:
            return False

        openn = {"(", "[", "{"}
        stack = []
        stack.append(s[0])
        i = 1

        while i < len(s): # stack not empty
            if s[i] in openn:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif self.isMatch(s[i], stack[-1]):
                    print(s[i])
                    stack.pop()
                else:
                    return False
            i+=1
            

        return len(stack) == 0

    def isMatch(self, close: str, open: str) -> bool:
        if close == ")" and open == "(":
            return True
        elif close == "]" and open == "[":
            return True
        elif close == "}" and open == "{":
            return True
        else:
            return False

    #Best solution
    def isValid2(self, s: str) -> bool:
        mapp = {")" : "(",
                "}" : "{",
                "]" : "["}
        stack = []

        for char in s:
            if char in mapp:
                if not stack:
                    return False
                if mapp[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
        
