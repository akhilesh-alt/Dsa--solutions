class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        stack=[]
        for i in range(n):
            if(s[i]=='('):
                stack.append(s[i])
            else:
                if(s[i]==')'):
                    if( stack and stack[-1]=='('):
                        stack.pop()
                    else:
                        return False
            if(s[i]=='{'):
                stack.append(s[i])
            else:
                if(s[i]=='}'):
                    if( stack and stack[-1]=='{'):
                        stack.pop()
                    else:
                        return False
            if(s[i]=='['):
                stack.append(s[i])
            else:
                if(s[i]==']'):
                    if( stack and stack[-1]=='['):
                        stack.pop()
                    else:
                        return False
        return len(stack)==0

        