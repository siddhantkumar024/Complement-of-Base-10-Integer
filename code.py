class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        b=[]
        while n >0:
            b.append(n%2)
            n=n//2
        print(b)
        for i in range(len(b)):
            if b[i]==1:
                b[i]=0
            else :
                b[i]=1
        print(b)    
        num=0
        for i in range (len(b)):
            if b[i]==1:
                num=num+2**i
        return num


        

        
