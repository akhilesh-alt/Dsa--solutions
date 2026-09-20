class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n=len(asteroids)
        st=[]
        for i in range(n):
            while len(st)>0 and asteroids[i]<0 and st[-1]>0:
                if(st[-1]>abs(asteroids[i])):
                    break
                elif(st[-1]==abs(asteroids[i])):
                    st.pop()
                    break
                elif(st[-1]<abs(asteroids[i])):
                    st.pop()
            else:
                st.append(asteroids[i])
        return st
        