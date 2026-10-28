class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        s=set()
        ans=float('inf')
        mp={}
        for w in list1:
            s.add(w)
        for w in list2:
            s.add(w)
        for x in s:
            if(x in list1 and x in list2):
                mp[x]=[]
                mp[x].append(list1.index(x))
                mp[x].append(list2.index(x))
        for x in mp.keys():
            ls=mp.get(x)
            summ=ls[0]+ls[1]
            ans=min(summ,ans)
        res=[]
        for x in mp.keys():
            ls=mp[x]
            if(ls[0]+ls[1]==ans):
                res.append(x)
        return res
        
        