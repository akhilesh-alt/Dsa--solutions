class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for ch in s:
            if(ch=='('):
                st.append(ch)
            elif(ch==')'):
                temp=[]
                while st[-1]!='(':
                    temp.append(st.pop())
                st.pop()
                for x in temp:
                    st.append(x)
            else:
                st.append(ch)
        return "".join(st)



    

        