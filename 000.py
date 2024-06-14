# 输入获取
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
 
 
# 并查集
class UnionFindSet:
    def __init__(self, n):
        self.fa = [idx for idx in range(n)]
        self.count = n
 
    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]
        return x
 
    def union(self, x, y):
        x_fa = self.find(x)
        y_fa = self.find(y)
 
        if x_fa != y_fa:
            self.fa[y_fa] = x_fa
            self.count -= 1
 
 
# 算法入口
def getResult():
    # 上、下、左、右、左上、左下、右上、右下的横坐标、纵坐标偏移量
    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
 
    # 记录所有边界位置
    brands = set()
 
    for i in range(m):
        for j in range(n):
            # 如果当前点是像素5
            if matrix[i][j] == 5:
                # 遍历像素5的相邻位置
                for offset in offsets:
                    newI = i + offset[0]
                    newJ = j + offset[1]
 
                    # 如果该位置不越界，且为像素1，则是边界
                    if m > newI >= 0 and n > newJ >= 0 and matrix[newI][newJ] == 1:
                        brands.add(newI * n + newJ)
 
    brands_list = list(brands)
    k = len(brands_list)
 
    # 使用并查集，对所有边界位置进行合并
    ufs = UnionFindSet(k)
 
    for i in range(k):
        x1 = brands_list[i] // n
        y1 = brands_list[i] % n
 
        for j in range(i + 1, k):
            x2 = brands_list[j] // n
            y2 = brands_list[j] % n
 
            # 如果两个边界像素1的位置 横向、纵向距离均小于1，则相邻，可以进行合并
            if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
                ufs.union(i, j)
 
    return ufs.count
 
 
# 算法调用
print(getResult())
