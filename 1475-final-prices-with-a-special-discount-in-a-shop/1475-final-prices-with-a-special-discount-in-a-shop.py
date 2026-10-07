def nex(prices,nse):
    st=[]
    for i in range(len(prices)):
        while len(st)!=0 and prices[i]<=prices[st[-1]]:
            nse[st[-1]]=i
            st.pop()
        st.append(i)
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n=len(prices)
        nse=[-1]*n
        nex(prices,nse)
        for i in range(len(prices)):
            if(nse[i]!=-1):
                prices[i]=prices[i]-prices[nse[i]]
        return prices


        