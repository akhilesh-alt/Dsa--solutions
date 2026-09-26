class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        """for i in range(n):
            for j in range(i,n):
                if(arr[i]==2*arr[j]):
                    return True
        return False"""
        s=set()
        for i in range(n):
            if(2*arr[i] in s):
                return True
            if(arr[i]%2==0):
                if(arr[i]//2 in s):
                    return True
            s.add(arr[i])
        return False

        