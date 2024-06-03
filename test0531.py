#part 1
n,total_amount,X=map(int,input().split())
return_list=list(map(int,input().split()))  #投资回报
risk_list=list(map(int,input().split()))   #风险系数
max_amount=list(map(int,input().split()))  #最大可投资额
max_return=0
pairs=[[0,0],[0,0]]
for i in range(n):
    for j in range(i+1,n):
        i_amount,j_amount=0,0
        if risk_list[i]+risk_list[j]>X:
            continue
        if max_amount[i]+max_amount[j]<=total_amount:
            i_amount=max_amount[i]
            j_amoumt=max_amount[j]
        else:
            if return_list[i]>=return_list[j]:
                i_amount=min(max_amount[i],total_amount)
                j_amount=total_amount-i_amount
            else:
                j_amount = min(max_amount[j], total_amount)
                i_amount = total_amount - j_amount
        cur_return = i_amount * return_list[i] + j_amount * return_list[j]
        if max_return<cur_return:
            max_return=cur_return
            pairs=[[i,i_amount],[j,j_amount]]
# print(pairs)
# print(max_return)
#考虑只选择一种产品的情况，得到的最大回报与考虑两种产品得到的最大回报相比较去最大值
for i in range(n):
    if risk_list[i]>X:
        continue
    i_amount=min(max_amount[i],total_amount)
    cur_return=i_amount*return_list[i]
    if max_return < cur_return:
        max_return = cur_return
        pairs = [[0,0], [i, i_amount]]
# print(pairs)
ans=[0]*n
ans[pairs[0][0]]=pairs[0][1]
ans[pairs[1][0]]=pairs[1][1]
print(" ".join(str(num) for num in ans))

#part 2
# 题目：【贪心】2023C-虚拟游戏理财
# 分值：200
# 作者：闭着眼睛学数理化
# 算法：贪心
# 代码看不懂的地方，请直接在群上提问


# 输入产品数量n，最大总投资额total_amount，最高风险系数X
n, total_amount, X = map(int, input().split())

# 输入长度为n的回报率列表
return_rate_lst = list(map(int, input().split()))

# 输入长度为n的风险值列表
risk_lst = list(map(int, input().split()))

# 输入长度为n的最大投资额序列
max_amount_lst = list(map(int, input().split()))

# 初始化总的最大回报值为0
max_return = 0
# 储存当前最大会值对应的产品编号以及所选取的份额数
pairs = [[0, 0], [0, 0]]

# 双重循环，遍历所有产品对（二元组）
for i in range(n):
    for j in range(i+1, n):
        # 考虑风险值的影响，如果两个产品的风险值加起来超过了X，则这组二元组不能选择
        # 直接跳过
        if risk_lst[i] + risk_lst[j] > X:
            continue
        # 如果两个产品的最大可投资额加起来，也不超过最大总投资额total_amount
        # 那么会贪心地将两个产品都选满
        # 即产品i选择max_amount_lst[i]份，产品j选择max_amount_lst[j]份
        if max_amount_lst[i] + max_amount_lst[j] <= total_amount:
            i_amount, j_amount = max_amount_lst[i], max_amount_lst[j]
        # 否则，我们必须在两个产品之间选择【单份产品的投资回报率】更高的产品
        # 贪心地尽可能选择它
        else:
            # 如果单份产品i的投资回报率更高
            if return_rate_lst[i] >= return_rate_lst[j]:
                # 产品i的份额，为产品i的最大额和总最大额之间的较小值
                i_amount = min(max_amount_lst[i], total_amount)
                # 产品j的份额，为总最大额减去产品i的份额
                j_amount = total_amount - i_amount
            # 如果单份产品j的投资回报率更高
            else:
                # 产品j的份额，为产品j的最大额和总最大额之间的较小值
                j_amount = min(max_amount_lst[j], total_amount)
                # 产品j的份额，为总最大额减去产品i的份额
                i_amount = total_amount - j_amount

        # 计算得到对应的当前回报值cur_return
        cur_return = i_amount * return_rate_lst[i] + j_amount * return_rate_lst[j]
        # 如果当前计算得到的回报值比之前记录过的最大回报值更大
        # 则更新最大回报值以及pairs
        if cur_return > max_return:
            max_return = cur_return
            pairs = [[i, i_amount], [j, j_amount]]


# 考虑只选择1种产品i的情况
for i in range(n):
    if risk_lst[i] > X:
        continue
    # 产品i的份额，为产品i的最大额和总最大额之间的较小值
    i_amount = min(max_amount_lst[i], total_amount)
    cur_return = i_amount * return_rate_lst[i]
    # 如果当前计算得到的回报值比之前记录过的最大回报值更大
    # 则更新最大回报值以及pairs
    if cur_return > max_return:
        max_return = cur_return
        pairs = [[0, 0], [i, i_amount]]


# 构建答案序列，除了最终的i和j位置需要调整为最优的i_amount和j_amount，
# 其他位置所选取的份额都是0
ans = [0] * n
ans[pairs[0][0]] = pairs[0][1]
ans[pairs[1][0]] = pairs[1][1]

print(" ".join(str(num) for num in ans))