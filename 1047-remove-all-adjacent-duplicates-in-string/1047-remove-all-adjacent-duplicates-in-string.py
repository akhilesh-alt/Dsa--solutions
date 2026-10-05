class Solution:
    def removeDuplicates(self, s: str) -> str:
        n=len(s)
        st=[]
        for i in range(n):
            if(len(st)!=0 and s[i]==st[-1]):
                st.pop()
            else:
                st.append(s[i])
        return "".join(st)

        