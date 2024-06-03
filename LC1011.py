class Solution:    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(loadweight):
            day=1
            i=0
            s=loadweight
            while i<=len(weights)-1:
                if loadweight>=weights[i]:
                    loadweight-=weights[i]
                    i+=1
                else:
                    day+=1
                    loadweight=s
                    if loadweight<weights[i]:
                        return 0
            if day<=days:
                return 1
            else:
                return 0
        left=1
        right=sum(weights)
        while left<right:
            mid=(left+right)//2
            if possible(mid):
                right=mid-1
            else:
                left=mid+1
        if possible(right):
            return right
        else:
            return right+1