class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path=[]
        result=[]
        def backtracking(n:int,k:int,startindex:int):
            if len(path)==k:
                result.append(path.copy())
                return
            for i in range(startindex,n+1):
                path.append(i)
                backtracking(n,k,i+1)
                path.pop()
        backtracking(n,k,1)
        return result